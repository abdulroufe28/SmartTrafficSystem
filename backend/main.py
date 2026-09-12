from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse,   StreamingResponse
from backend.services import video_stream
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
from backend.routes.traffic_api import router as traffic_router 

app = FastAPI()

app.include_router(traffic_router)

app.mount("/static", StaticFiles(directory="backend/static"), name="static")

templates = Jinja2Templates(directory="backend/templates")


@app.get("/")
def login_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="login.html"
    )


@app.get("/dashboard")
def dashboard_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html"
    )


@app.get("/analytics")
def analytics(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="analytics.html"
    )


@app.get("/emergency")
def emergency(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="emergency.html"
    )


@app.get("/signals")
def signals(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="signals.html"
    )


@app.get("/reports")
def reports(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="reports.html"
    )


@app.get("/settings")
def settings(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="settings.html"
    )

@app.get("/download-report")
async def download_report():

    file_path = "backend/reports/traffic_report.txt"

    with open(file_path, "w") as file:

        file.write("SMART TRAFFIC MANAGEMENT REPORT\n\n")

        file.write("Total Vehicles Detected : 542\n")

        file.write("Traffic Density : MEDIUM\n")

        file.write("Emergency Alerts : 4\n")

        file.write("AI Monitoring Status : ACTIVE\n")

    return FileResponse(
        path=file_path,
        filename="traffic_report.txt",
        media_type="text/plain"
    )


@app.get("/download-csv")
async def download_csv():

    file_path = "backend/reports/traffic_data.csv"

    with open(file_path, "w") as file:

        file.write("Date,Vehicles,Density,Emergencies\n")

        file.write("15-05-2026,542,Medium,4\n")

        file.write("14-05-2026,612,High,7\n")

        file.write("13-05-2026,430,Low,2\n")

    return FileResponse(
        path=file_path,
        filename="traffic_data.csv",
        media_type="text/csv"
    )

@app.get("/video_feed")


def video_feed():

    return StreamingResponse(
        video_stream.generate_frames(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )

@app.get("/slow_video_feed")

async def slow_video_feed():

    return StreamingResponse(

        video_stream.generate_slow_frames(),

        media_type=
        "multipart/x-mixed-replace; boundary=frame"

    )


@app.get("/traffic_data")

async def traffic_data():

    return {

        "vehicle_count":
        video_stream.live_vehicle_count,

        "traffic_density":
        video_stream.traffic_density,

        "signal_time":
        video_stream.signal_time,

        "emergency_status":
        video_stream.emergency_status

    }