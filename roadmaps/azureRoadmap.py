import os
from datetime import datetime, timedelta

current_dir = os.getcwd()
os.chdir("./roadmaps/")

def move_date(date_str, days):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    new_date = date + timedelta(days=days)
    return new_date.strftime("%Y-%m-%d")

def azure_cloud_foundations_road_map_generations():

    from roadmapper.roadmap import Roadmap
    from roadmapper.timelinemode import TimelineMode

    roadmap = Roadmap(
            1400, 1000, auto_height=True, show_marker=True
        )
    roadmap.set_title("Azure Cloud Foundations ROADMAP 2024")
    roadmap.set_subtitle("Legal and General Cloud Engineering")
    roadmap.add_logo("lg-logo.jpg", position="top-right", width=75, height=75)
    roadmap.set_timeline(
        mode = TimelineMode.MONTHLY,
        start = move_date("2024-02-01", 0),  # Start date moved by one month
        number_of_items = 16,
        show_generic_dates=False,
        year_fill_colour="#008AD7",
        year_font_colour="white",
        item_fill_colour="#008AD7",
        item_font_colour="white",
    )

    # Planning
    group = roadmap.add_group("Planning", fill_colour="#028844", font_colour="white")
    
    task = group.add_task(
       "Tranfer Azure CF", move_date("2024-02-01", 0), move_date("2024-04-15", 0), fill_colour="#028844", font_colour="white"
    )
    task.add_parallel_task(
       "Azure GAP Analysis", move_date("2024-04-18", 0), move_date("2024-06-30", 0), fill_colour="#028844", font_colour="white"
    )

    task = group.add_task(
       "Azure Resource Profile", move_date("2024-04-01", 0), move_date("2024-07-15", 0), fill_colour="#028844", font_colour="white"
    )

    task.add_milestone(
        "SRE Team Onboarded", move_date("2024-10-20", 0), fill_colour="#005629", font_colour="#005629"
    )

    task = group.add_task(
       "Network Design Review", move_date("2024-05-01", 0), move_date("2024-07-20", 0), fill_colour="#028844", font_colour="white"
    )

    task.add_parallel_task(
        "Network Firewalls",
        move_date("2024-07-21", 0),
        move_date("2024-09-30", 0),
        fill_colour="#028844",
        font_colour="white",
    )

    task.add_milestone(
        "RfP Awarded", move_date("2024-06-20", 0), fill_colour="#005629", font_colour="#005629"
    )

    # Strategy
    group = roadmap.add_group("California", fill_colour="#FFD500", font_colour="black")
    task = group.add_task(
        "Internal Cloud Analysis",
        move_date("2024-03-01", 0),
        move_date("2024-05-20", 0),
        fill_colour="#FFD500",
        font_colour="black",
    )
    task.add_milestone(
        "Audit HR1.1 Due", move_date("2024-06-15", 0), fill_colour="#DD9C00", font_colour="#DD9C00"
    )

    task.add_milestone(
        "Audit HR1.2 Due", move_date("2024-10-15", 0), fill_colour="#DD9C00", font_colour="#DD9C00"
    )

    task.add_milestone(
        "Audit HR1.3 Due", move_date("2024-12-15", 0), fill_colour="#DD9C00", font_colour="#DD9C00"
    )

    task.add_milestone(
        "Audit HR1.4 Due", move_date("2025-01-30", 0), fill_colour="#DD9C00", font_colour="#DD9C00"
    )

    task = group.add_task(
        "FinOps and Financial Reporting",
        move_date("2024-02-01", 0),
        move_date("2024-12-20", 0),
        fill_colour="#FFD500",
        font_colour="black",
    )

    task = group.add_task(
        "New Cloud Operating Model",
        move_date("2024-07-01", 0),
        move_date("2024-10-20", 0),
        fill_colour="#FFD500",
        font_colour="black",
    )

    # Service Development
    group = roadmap.add_group(
        "Product Development", fill_colour="#E22922", font_colour="white"
    )

    task = group.add_task(
       "GitHub Integration",
       move_date("2024-03-10", 0),
       move_date("2024-05-10", 0),
        fill_colour="#E22922",
        font_colour="white",
    )

    parallel_task = task.add_parallel_task(
        "GitHub Backup",
        move_date("2024-05-05", 0),
        move_date("2024-06-30", 0),
        fill_colour="#E22922",
        font_colour="white",
    )

    parallel_task = task.add_parallel_task(
        "GitHub Migrations",
        move_date("2024-06-30", 0),
        move_date("2024-08-25", 0),
        fill_colour="#E22922",
        font_colour="white",
    )

    parallel_task.add_milestone(
        "Service Readiness: GitHub", move_date("2024-08-30", 0), fill_colour="#A81815", font_colour="#A81815"
    )

    task = group.add_task(
       "Tranfer: Supplier to Group Technology",
       move_date("2024-11-10", 0),
       move_date("2025-05-10", 0),
        fill_colour="#E22922",
        font_colour="white",
    )

    task = group.add_task(
       "Documentation Improvements",
       move_date("2024-04-15", 0),
       move_date("2024-09-10", 0),
        fill_colour="#E22922",
        font_colour="white",
    )

    task = group.add_task(
       "Service Now Form Improvements",
       move_date("2024-04-15", 0),
       move_date("2024-09-10", 0),
        fill_colour="#E22922",
        font_colour="white",
    )

    parallel_task = task.add_parallel_task(
        "Seamless Account Vending",
        move_date("2024-09-10", 0),
        move_date("2025-01-30", 0),
        fill_colour="#E22922",
        font_colour="white",
    )

    task = group.add_task(
        "Preventative Guardrails",
        move_date("2024-02-26", 0),
        move_date("2025-03-16", 0),
        fill_colour="#E22922",
        font_colour="white",
    )

    task = group.add_task(
        "Product Roadmap",
        move_date("2024-05-26", 0),
        move_date("2024-10-16", 0),
        fill_colour="#E22922",
        font_colour="white",
    )
  
    parallel_task.add_milestone(
        "Azure CF v1.0", move_date("2024-11-10", 0), fill_colour="#A81815", font_colour="#A81815"
    )
    parallel_task.add_milestone(
        "Azure v2.0", move_date("2025-05-10", 0), fill_colour="#A81815", font_colour="#A81815"
    )

    # Platform 
    group = roadmap.add_group("Platform & Engineering", fill_colour="#333333", font_colour="white")

    task = group.add_task(
       "Terraform Enterprise Integration",
       move_date("2024-04-15", 0),
       move_date("2024-09-10", 0),
        fill_colour="#333333",
        font_colour="white",
    )

    # Operations
    group = roadmap.add_group(
        "Operations",
        fill_colour="#4472C4",
        font_colour="white",
    )

    task = group.add_task(
        "CSMP Integration",
        move_date("2024-06-30", 0),
        move_date("2024-10-29", 0),
        fill_colour="#4472C4",
        font_colour="white",
    )

    task = group.add_task(
        "Lighthouse Control Framework",
        move_date("2024-04-30", 0),
        move_date("2024-10-29", 0),
        fill_colour="#4472C4",
        font_colour="white",
    )
    
    
    task = group.add_task(
        "Splunk Integration",
        move_date("2024-06-15", 0),
        move_date("2024-08-29", 0),
        fill_colour="#4472C4",
        font_colour="white",
    )

    task = group.add_task(
        "Sailpoint Integration",
        move_date("2024-06-15", 0),
        move_date("2024-08-29", 0),
        fill_colour="#4472C4",
        font_colour="white",
    )

    parallel_task = task.add_parallel_task(
        "RBAC Design",
        move_date("2024-08-29", 0),
        move_date("2024-10-15", 0),
        fill_colour="#4472C4",
        font_colour="white",
    )

    task = group.add_task(
        "Grafana Integration",
        move_date("2024-07-15", 0),
        move_date("2024-09-29", 0),
        fill_colour="#4472C4",
        font_colour="white",
    )

    parallel_task = task.add_parallel_task(
        "Monitoring Dashboards",
        move_date("2024-10-01", 0),
        move_date("2024-12-15", 0),
        fill_colour="#4472C4",
        font_colour="white",
    )

    parallel_task = task.add_parallel_task(
        "Oncall and incident management",
        move_date("2024-12-17", 0),
        move_date("2025-04-15", 0),
        fill_colour="#4472C4",
        font_colour="white",
    )

    parallel_task.add_milestone(
        "Service Readiness:Grafana", move_date("2024-09-25", 0), fill_colour="#004E86", font_colour="#004E86"
    )
    
    roadmap.set_footer("Designed by Group Cloud Engineering")
    roadmap.draw()

    roadmap.save("azure-cloud-foundations-roadmap.png")

def main():
  azure_cloud_foundations_road_map_generations()

if __name__ == '__main__':
  main()
