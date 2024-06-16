import os

current_dir = os.getcwd()
os.chdir("./roadmaps/")

def cloud_operations_road_map_generations():

    from roadmapper.roadmap import Roadmap
    from roadmapper.timelinemode import TimelineMode

    roadmap = Roadmap(
            1400, 1000, auto_height=True, show_marker=True
        )
    roadmap.set_title("Cloud Operations ROADMAP 2024")
    roadmap.set_subtitle("Legal and General Cloud Engineering")
    roadmap.add_logo("lg-logo.jpg", position="top-right", width=75, height=75)
    roadmap.set_timeline(
        mode = TimelineMode.MONTHLY,
        start = "2024-01-01",
        number_of_items = 16,
        show_generic_dates=False,
        year_fill_colour="#0076D6",
        year_font_colour="white",
        item_fill_colour="#0076D6",
        item_font_colour="white",
    )

    # Monitoring and Incident Management
    group = roadmap.add_group("Monitoring & Incident Management", fill_colour="#028844", font_colour="white")
    
    task = group.add_task(
       "Implement Centralized Logging", "2024-01-01","2024-03-31",  fill_colour="#028844", font_colour="white"
    )
    task.add_parallel_task(
       "Set Up Monitoring Dashboards", "2024-04-01", "2024-06-30", fill_colour="#028844", font_colour="white"
    )

    task = group.add_task(
       "Automate Incident Response", "2024-07-01","2024-09-30",  fill_colour="#028844", font_colour="white"
    )
    task.add_milestone(
        "Incident Automation Live", "2024-10-15", fill_colour="#005629", font_colour="#005629"
    )

    # Security and Compliance
    group = roadmap.add_group("Security & Compliance", fill_colour="#FFD500", font_colour="black")
    task = group.add_task(
        "Implement Security Best Practices", "2024-01-15", "2024-03-15", fill_colour="#FFD500", font_colour="black",
    )
    task.add_milestone(
        "Security Practices Implemented", "2024-03-20", fill_colour="#DD9C00", font_colour="#DD9C00"
    )

    task = group.add_task(
        "Conduct Security Audits", "2024-04-01", "2024-06-30", fill_colour="#FFD500", font_colour="black",
    )
    task.add_milestone(
        "Security Audit Complete", "2024-07-01", fill_colour="#DD9C00", font_colour="#DD9C00"
    )

    task = group.add_task(
        "Continuous Compliance Monitoring", "2024-07-01", "2024-12-31", fill_colour="#FFD500", font_colour="black",
    )

    # Infrastructure Management
    group = roadmap.add_group("Infrastructure Management", fill_colour="#E22922", font_colour="white")

    task = group.add_task(
       "Infrastructure as Code Implementation", "2024-01-10", "2024-03-31", fill_colour="#E22922", font_colour="white",
    )
    task.add_parallel_task(
        "Cloud Resource Optimization", "2024-04-01", "2024-06-30", fill_colour="#E22922", font_colour="white",
    )
    task.add_milestone(
        "Optimization Report Published", "2024-07-01", fill_colour="#A81815", font_colour="#A81815"
    )

    task = group.add_task(
       "Multi-Cloud Strategy Development", "2024-07-01", "2024-09-30", fill_colour="#E22922", font_colour="white",
    )

    # Service Management
    group = roadmap.add_group("Service Management", fill_colour="#333333", font_colour="white")

    task = group.add_task(
       "Service Catalog Development", "2024-01-15", "2024-03-31", fill_colour="#333333", font_colour="white",
    )
    task.add_parallel_task(
        "Service Level Agreements (SLAs)", "2024-04-01", "2024-06-30", fill_colour="#333333", font_colour="white",
    )
    task.add_milestone(
        "SLAs Published", "2024-07-01", fill_colour="#555555", font_colour="#555555"
    )

    task = group.add_task(
       "Service Improvement Plan", "2024-07-01", "2024-09-30", fill_colour="#333333", font_colour="white",
    )

    # Automation and Efficiency
    group = roadmap.add_group("Automation & Efficiency", fill_colour="#4472C4", font_colour="white")

    task = group.add_task(
        "Develop Automation Scripts", "2024-01-15", "2024-04-15", fill_colour="#4472C4", font_colour="white",
    )
    task.add_milestone(
        "Automation Scripts Ready", "2024-04-20", fill_colour="#004E86", font_colour="#004E86"
    )

    task = group.add_task(
        "Implement CI/CD Pipelines", "2024-05-01", "2024-08-01", fill_colour="#4472C4", font_colour="white",
    )
    task.add_milestone(
        "CI/CD Pipelines Live", "2024-08-15", fill_colour="#004E86", font_colour="#004E86"
    )

    roadmap.set_footer("Designed by Group Cloud Engineering")
    roadmap.draw()

    roadmap.save("cloud-operations-roadmap.png")

def main():
  cloud_operations_road_map_generations()

if __name__ == '__main__':
  main()
