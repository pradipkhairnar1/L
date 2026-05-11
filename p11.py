class ExpertSystem:

    # Function to evaluate employee
    def evaluate(self):

        print("=== Employee Performance System ===")

        # Taking input
        attendance = int(input("Enter attendance percentage: "))
        work = int(input("Enter work quality marks: "))
        teamwork = int(input("Enter teamwork marks: "))

        # Rules
        if attendance >= 90 and work >= 8 and teamwork >= 8:
            result = "Excellent"

        elif attendance >= 75 and work >= 6 and teamwork >= 6:
            result = "Good"

        elif attendance >= 60 and work >= 5 and teamwork >= 5:
            result = "Average"

        else:
            result = "Poor"

        # Display result
        print("\nEmployee Performance:", result)


# Main program
system = ExpertSystem()

system.evaluate()




class EmployeeExpertSystem:

    def __init__(self):

        # Knowledge base (rules)
        self.rules = [
            {
                "name": "Excellent",
                "conditions": {
                    "attendance": 90,
                    "work_quality": 8,
                    "teamwork": 8
                },
                "bonus": "High Bonus"
            },

            {
                "name": "Good",
                "conditions": {
                    "attendance": 75,
                    "work_quality": 6,
                    "teamwork": 6
                },
                "bonus": "Medium Bonus"
            },

            {
                "name": "Average",
                "conditions": {
                    "attendance": 60,
                    "work_quality": 5,
                    "teamwork": 5
                },
                "bonus": "Low Bonus"
            }
        ]

    # Taking employee details
    def get_employee_data(self):

        print("=== Employee Performance Expert System ===")

        attendance = int(input("Enter attendance percentage: "))
        work_quality = int(input("Enter work quality marks (out of 10): "))
        teamwork = int(input("Enter teamwork marks (out of 10): "))

        return {
            "attendance": attendance,
            "work_quality": work_quality,
            "teamwork": teamwork
        }

    # Inference engine
    def evaluate(self, data):

        for rule in self.rules:

            conditions = rule["conditions"]

            if (
                data["attendance"] >= conditions["attendance"]
                and data["work_quality"] >= conditions["work_quality"]
                and data["teamwork"] >= conditions["teamwork"]
            ):

                return {
                    "performance": rule["name"],
                    "bonus": rule["bonus"]
                }

        return {
            "performance": "Poor",
            "bonus": "No Bonus"
        }

    # Display result
    def explain(self, result):

        print("\n=== Evaluation Result ===")

        print("Performance :", result["performance"])
        print("Bonus Status:", result["bonus"])

    # Main function
    def run(self):

        data = self.get_employee_data()

        result = self.evaluate(data)

        self.explain(result)


# Program starts here
if __name__ == "__main__":

    system = EmployeeExpertSystem()

    system.run()



