import os

current_dir = os.getcwd()
os.chdir("./roadmaps/")

def azure_finops_road_map_generations():

    from roadmapper.roadmap import Roadmap
    from roadmapper.timelinemode import TimelineMode

    roadmap = Roadmap(
            1400, 1000, auto_height=True, show_marker=True
        )
    roadmap.set_title("FinOps ROADMAP 2024")
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

    # Cost Management and Optimization
    group = roadmap.add_group("Cost Management & Optimization", fill_colour="#028844", font_colour="white")
    
    task = group.add_task(
       "Implement Cost Allocation Tags", "2024-01-01","2024-02-28",  fill_colour="#028844", font_colour="white"
    )
    task.add_parallel_task(
       "Review Reserved Instances", "2024-03-01", "2024-04-30", fill_colour="#028844", font_colour="white"
    )

    task = group.add_task(
       "Cost Optimization Analysis", "2024-05-01","2024-07-31",  fill_colour="#028844", font_colour="white"
    )
    task.add_milestone(
        "Optimization Report Published", "2024-08-15", fill_colour="#005629", font_colour="#005629"
    )

    # Budgeting and Forecasting
    group = roadmap.add_group("Budgeting & Forecasting", fill_colour="#FFD500", font_colour="black")
    task = group.add_task(
        "Set Up Budget Alerts", "2024-02-01", "2024-03-15", fill_colour="#FFD500", font_colour="black",
    )
    task.add_milestone(
        "Budget Alerts Active", "2024-03-20", fill_colour="#DD9C00", font_colour="#DD9C00"
    )

    task = group.add_task(
        "Quarterly Spend Forecasting", "2024-01-15", "2024-12-15", fill_colour="#FFD500", font_colour="black",
    )
    task.add_milestone(
        "Q1 Forecast Complete", "2024-03-31", fill_colour="#DD9C00", font_colour="#DD9C00"
    )
    task.add_milestone(
        "Q2 Forecast Complete", "2024-06-30", fill_colour="#DD9C00", font_colour="#DD9C00"
    )
    task.add_milestone(
        "Q3 Forecast Complete", "2024-09-30", fill_colour="#DD9C00", font_colour="#DD9C00"
    )
    task.add_milestone(
        "Q4 Forecast Complete", "2024-12-31", fill_colour="#DD9C00", font_colour="#DD9C00"
    )

    # Financial Reporting and Transparency
    group = roadmap.add_group("Financial Reporting & Transparency", fill_colour="#E22922", font_colour="white")

    task = group.add_task(
       "Develop FinOps Dashboard", "2024-01-10", "2024-04-10", fill_colour="#E22922", font_colour="white",
    )
    parallel_task = task.add_parallel_task(
        "Integrate with BI Tools", "2024-04-15", "2024-06-30", fill_colour="#E22922", font_colour="white",
    )
    parallel_task.add_milestone(
        "Dashboard Live", "2024-07-01", fill_colour="#A81815", font_colour="#A81815"
    )

    task = group.add_task(
       "Monthly Spend Reports", "2024-01-15", "2024-12-31", fill_colour="#E22922", font_colour="white",
    )

    # Governance and Compliance
    group = roadmap.add_group("Governance & Compliance", fill_colour="#333333", font_colour="white")

    task = group.add_task(
       "Policy Review and Update", "2024-03-01", "2024-06-01", fill_colour="#333333", font_colour="white",
    )
    task.add_parallel_task(
        "Compliance Audits", "2024-06-15", "2024-09-30", fill_colour="#333333", font_colour="white",
    )
    task.add_milestone(
        "Audit Report Published", "2024-10-10", fill_colour="#555555", font_colour="#555555"
    )

    # Continuous Improvement
    group = roadmap.add_group("Continuous Improvement", fill_colour="#4472C4", font_colour="white")

    task = group.add_task(
        "Regular FinOps Reviews", "2024-01-15", "2024-12-15", fill_colour="#4472C4", font_colour="white",
    )
    task.add_milestone(
        "Review Meeting Q1", "2024-03-31", fill_colour="#004E86", font_colour="#004E86"
    )
    task.add_milestone(
        "Review Meeting Q2", "2024-06-30", fill_colour="#004E86", font_colour="#004E86"
    )
    task.add_milestone(
        "Review Meeting Q3", "2024-09-30", fill_colour="#004E86", font_colour="#004E86"
    )
    task.add_milestone(
        "Review Meeting Q4", "2024-12-31", fill_colour="#004E86", font_colour="#004E86"
    )

    roadmap.set_footer("Designed by Group Cloud Engineering")
    roadmap.draw()

    roadmap.save("azure-finops-roadmap.png")

def main():
  azure_finops_road_map_generations()

if __name__ == '__main__':
  main()
