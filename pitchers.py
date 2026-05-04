def pitcher_profile(df):
    pitchers = df.groupby("pitcher").agg({
        "launch_speed": "mean",
        "barrel": "mean",
        "events": lambda x: (x == "home_run").mean()
    }).reset_index()

    pitchers.rename(columns={
        "launch_speed": "ev_allowed",
        "barrel": "barrel_rate_allowed",
        "events": "hr_rate_allowed"
    }, inplace=True)

    return pitchers
