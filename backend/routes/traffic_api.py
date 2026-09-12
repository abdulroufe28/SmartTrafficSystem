from fastapi import APIRouter
import backend.services.video_stream as video_stream

router = APIRouter()

@router.get("/traffic-data")
def get_traffic_data():

    count = video_stream.live_vehicle_count

    print("LIVE COUNT:", count)

    density = "LOW"

    if count > 10:
        density = "MEDIUM"

    if count > 20:
        density = "HIGH"

    return {
        "total_vehicles": count,
        "traffic_density": density,
        "emergency_vehicles": 1,
        "active_signals": 4
    }