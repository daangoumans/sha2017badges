import badge, easydraw, time, appglue

easydraw.msg("","Sweary", True)

enabled = badge.nvs_get_u8("sweary","enable", 0)
if enabled:
    enabled = 0
    easydraw.msg("Sweary disabled!")
else:
    enabled = 1
    easydraw.msg("Sweary enabled!")
    easydraw.msg("Go back to the splash and wait...")
enabled = badge.nvs_set_u8("sweary","enable", enabled)

time.sleep(5)
appglue.home()
