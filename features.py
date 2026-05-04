def build_features(hitter, pitcher, weather_score):
    return (
        0.35 * hitter["barrel_rate"] +
        0.25 * hitter["avg_ev"] / 100 +
        0.20 * hitter["hr_form"] +
        0.15 * pitcher["hr_rate_allowed"] +
        0.05 * weather_score
    )
