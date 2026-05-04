def weather_boost(temp, wind_speed, wind_out):
    score = 0

    if temp > 25:
        score += 0.1
    if wind_speed > 10 and wind_out:
        score += 0.15
    if temp > 30:
        score += 0.2

    return min(score, 0.3)
