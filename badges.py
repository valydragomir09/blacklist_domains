from pybadges import badge
from datetime import date

# Create a badge for build Last update
last_update_badge = badge(
    left_text="Last update",
    right_text=str(date.today()),
    right_color="blue",
)

# Save the badge to a file
with open("img/last_update_badge.svg", "w") as f:
    f.write(last_update_badge)

# Create a badge for build Total domains
with open("casino_domains.txt", "r") as f:
    data = f.read()
domains = data.splitlines()
    
total_domains_badge = badge(
    left_text="Total domains:", 
    right_text="%s" % len(domains),
    right_color='red'
)

# Save the badge to a file
with open("img/total_domains_badge.svg", "w") as f:
    f.write(total_domains_badge)

# Print the badge SVG content
# print(last_update_badge)
# print(total_domains_badge)