import ephem
from datetime import datetime

def calculate_moon_phase() -> dict:
    """
    Calculates the current moon phase based on today's date.
    """
    moon = ephem.Moon(datetime.utcnow())
    phase = moon.phase  # 0 = new moon, 14.77 = full moon

    def get_phase_name(phase_val: float) -> str:
        if phase_val < 1.0:
            return "New Moon"
        elif phase_val < 7.4:
            return "Waxing Crescent"
        elif phase_val < 8.6:
            return "First Quarter"
        elif phase_val < 13.8:
            return "Waxing Gibbous"
        elif phase_val < 15.8:
            return "Full Moon"
        elif phase_val < 21.0:
            return "Waning Gibbous"
        elif phase_val < 22.1:
            return "Last Quarter"
        else:
            return "Waning Crescent"

    return {
        "indicator": "moon_phases",
        "phase_value": round(phase, 2),
        "phase_name": get_phase_name(phase)
    }
