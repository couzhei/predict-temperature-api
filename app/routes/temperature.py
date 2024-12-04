from fastapi import APIRouter

router = APIRouter()

@router.get("/temperature/next-10-days")
def get_temperatures():
    return {
        "location": "New York",
        "predictions": [
            # Day : temperature
            {"2024-12-04": 10},
            {"2024-12-05": 11},
        ]
    }
