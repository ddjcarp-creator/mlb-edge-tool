def matchup_score(hitter, pitcher):
    return (
        hitter["barrel_rate"] * 0.4 +
        hitter["avg_ev"] / 100 * 0.3 +
        pitcher["hr_rate_allowed"] * 0.3
    )
