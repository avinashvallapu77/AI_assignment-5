from flask import Flask, request, jsonify

app = Flask(__name__)

# Knowledge Base
destinations = {
    "Goa": {
        "budget": 15000,
        "food": ["Sea Food", "Goan Curry", "Bebinca"],
        "places": ["Baga Beach", "Fort Aguada", "Anjuna Beach"],
        "best_time": "November to February"
    },

    "Manali": {
        "budget": 12000,
        "food": ["Momos", "Thukpa", "Siddu"],
        "places": ["Solang Valley", "Rohtang Pass", "Mall Road"],
        "best_time": "October to June"
    },

    "Jaipur": {
        "budget": 10000,
        "food": ["Dal Baati Churma", "Ghewar"],
        "places": ["Hawa Mahal", "Amber Fort", "City Palace"],
        "best_time": "November to March"
    }
}


# -------------------------------
# Travel Planner Class
# -------------------------------
class TravelPlanner:

    def recommend_destination(self, budget):
        recommendations = []

        for city, details in destinations.items():
            if details["budget"] <= budget:
                recommendations.append({
                    "city": city,
                    "estimated_budget": details["budget"],
                    "recommended_food": details["food"],
                    "tourist_places": details["places"],
                    "best_time_to_visit": details["best_time"]
                })

        return recommendations

    def estimate_trip_cost(self, hotel, food, transport):
        total = hotel + food + transport
        return total


planner = TravelPlanner()


# -------------------------------
# API Routes
# -------------------------------

@app.route('/')
def home():
    return """
    <h1>AI Based Travel Planner</h1>
    <p>Available APIs:</p>

    <ul>
        <li>/recommend?budget=15000</li>
        <li>/estimate?hotel=5000&food=3000&transport=2000</li>
    </ul>
    """


# Destination Recommendation API
@app.route('/recommend', methods=['GET'])
def recommend():
    budget = request.args.get('budget')

    if budget is None:
        return jsonify({"error": "Please provide budget"}), 400

    budget = int(budget)

    result = planner.recommend_destination(budget)

    if not result:
        return jsonify({
            "message": "No destinations available within this budget"
        })

    return jsonify(result)


# Budget Estimation API
@app.route('/estimate', methods=['GET'])
def estimate():
    hotel = int(request.args.get('hotel', 0))
    food = int(request.args.get('food', 0))
    transport = int(request.args.get('transport', 0))

    total = planner.estimate_trip_cost(hotel, food, transport)

    return jsonify({
        "hotel_cost": hotel,
        "food_cost": food,
        "transport_cost": transport,
        "total_trip_cost": total
    })


# -------------------------------
# Main Function
# -------------------------------
if __name__ == '__main__':
    app.run(debug=True)
