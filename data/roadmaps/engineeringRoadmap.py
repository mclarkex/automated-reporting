import os

current_dir = os.getcwd()
os.chdir("./roadmaps/")

def cloud_engineering_strategy_road_map_generations():

    from roadmapper.roadmap import Roadmap
    from roadmapper.timelinemode import TimelineMode

    roadmap = Roadmap(
            1600, 1200, auto_height=True, show_marker=True
        )
    roadmap.set_title("Cloud Engineering Strategy ROADMAP 2024-2025")
    roadmap.set_subtitle("Legal and General Cloud Engineering")
    roadmap.add_logo("lg-logo.jpg", position="top-right", width=75, height=75)
    roadmap.set_timeline(
        mode = TimelineMode.MONTHLY,
        start = "2024-01-01",
        number_of_items = 24,
        show_generic_dates=False,
        year_fill_colour="#0076D6",
        year_font_colour="white",
        item_fill_colour="#0076D6",
        item_font_colour="white",
    )

    # Strategic Initiatives
    group = roadmap.add_group("Strategic Initiatives", fill_colour="#028844", font_colour="white")
    
    task = group.add_task(
       "Group Cloud Engineering Strategy 2024", "2024-01-01","2024-03-31",  fill_colour="#028844", font_colour="white"
    )
    task.add_parallel_task(
       "2023 Assessment & Analysis", "2024-01-15", "2024-02-28", fill_colour="#028844", font_colour="white"
    )
    task.add_parallel_task(
       "AWS Cloud Foundations Remediation", "2024-03-01", "2024-06-30", fill_colour="#028844", font_colour="white"
    )
    task.add_parallel_task(
       "Azure Cloud Foundations Strategy", "2024-04-01", "2024-06-30", fill_colour="#028844", font_colour="white"
    )

    task = group.add_task(
       "FinOps Strategy", "2024-07-01","2024-09-30",  fill_colour="#028844", font_colour="white"
    )
    task.add_milestone(
        "FinOps Strategy Implemented", "2024-10-15", fill_colour="#005629", font_colour="#005629"
    )

    task = group.add_task(
       "2025 Strategic Planning", "2024-10-01", "2024-12-31", fill_colour="#028844", font_colour="white",
    )
    task.add_milestone(
        "2025 Strategy Finalized", "2024-12-31", fill_colour="#005629", font_colour="#005629"
    )

    task = group.add_task(
       "2025 Initiatives Kickoff", "2025-01-01", "2025-03-31", fill_colour="#028844", font_colour="white",
    )

    # Cloud Efficiency and Support Models
    group = roadmap.add_group("Cloud Efficiency & Support Models", fill_colour="#FFD500", font_colour="black")
    task = group.add_task(
        "Cloud Efficiency Ratio Improvement", "2024-01-15", "2024-03-15", fill_colour="#FFD500", font_colour="black",
    )
    task.add_milestone(
        "Efficiency Ratio Improved", "2024-03-20", fill_colour="#DD9C00", font_colour="#DD9C00"
    )

    task = group.add_task(
        "Workshops & Training", "2024-04-01", "2024-06-30", fill_colour="#FFD500", font_colour="black",
    )
    task.add_parallel_task(
        "Asymmetric Operational Support Model", "2024-07-01", "2024-09-30", fill_colour="#FFD500", font_colour="black",
    )
    task.add_milestone(
        "Support Model Implemented", "2024-10-01", fill_colour="#DD9C00", font_colour="#DD9C00"
    )

    task = group.add_task(
        "Group Digital and Experience Platform Support", "2024-05-01", "2024-07-31", fill_colour="#FFD500", font_colour="black",
    )
    task.add_milestone(
        "Platform Support Live", "2024-08-01", fill_colour="#DD9C00", font_colour="#DD9C00"
    )

    task = group.add_task(
       "Enhanced Support Model for LGIM", "2024-08-01", "2024-11-30", fill_colour="#FFD500", font_colour="black",
    )
    task.add_milestone(
        "LGIM Support Model Live", "2024-12-01", fill_colour="#DD9C00", font_colour="#DD9C00"
    )

    # Learning and Development
    group = roadmap.add_group("Learning & Development", fill_colour="#E22922", font_colour="white")

    task = group.add_task(
       "Learning & Development Strategy", "2024-01-10", "2024-03-31", fill_colour="#E22922", font_colour="white",
    )
    task.add_parallel_task(
        "Observability, Data & Management Information Strategy", "2024-04-01", "2024-06-30", fill_colour="#E22922", font_colour="white",
    )
    task.add_milestone(
        "Strategies Implemented", "2024-07-01", fill_colour="#A81815", font_colour="#A81815"
    )

    task = group.add_task(
       "Cloud Engineering Standards", "2024-07-01", "2024-09-30", fill_colour="#E22922", font_colour="white",
    )
    task.add_milestone(
        "Engineering Standards Implemented", "2024-10-01", fill_colour="#A81815", font_colour="#A81815"
    )

    task = group.add_task(
       "Continuous Learning Program", "2025-01-01", "2025-06-30", fill_colour="#E22922", font_colour="white",
    )
    task.add_milestone(
        "Continuous Learning Launched", "2025-07-01", fill_colour="#A81815", font_colour="#A81815"
    )

    # Operational Excellence
    group = roadmap.add_group("Operational Excellence", fill_colour="#333333", font_colour="white")

    task = group.add_task(
       "Observability Implementation", "2024-01-15", "2024-03-31", fill_colour="#333333", font_colour="white",
    )
    task.add_parallel_task(
        "Operational Excellence Framework", "2024-04-01", "2024-06-30", fill_colour="#333333", font_colour="white",
    )
    task.add_milestone(
        "Excellence Framework Live", "2024-07-01", fill_colour="#555555", font_colour="#555555"
    )

    task = group.add_task(
       "Sustainability Initiatives", "2024-07-01", "2024-09-30", fill_colour="#333333", font_colour="white",
    )
    task.add_parallel_task(
        "Operational Excellence Audit", "2024-10-01", "2024-12-31", fill_colour="#333333", font_colour="white",
    )
    task.add_milestone(
        "Operational Audit Complete", "2025-01-15", fill_colour="#555555", font_colour="#555555"
    )

    task = group.add_task(
       "Operational Excellence Program", "2025-02-01", "2025-06-30", fill_colour="#333333", font_colour="white",
    )
    task.add_milestone(
        "Operational Excellence Achieved", "2025-07-01", fill_colour="#555555", font_colour="#555555"
    )

    # Security and Compliance
    group = roadmap.add_group("Security & Compliance", fill_colour="#4472C4", font_colour="white")

    task = group.add_task(
        "Security Enhancements", "2024-01-15", "2024-04-15", fill_colour="#4472C4", font_colour="white",
    )
    task.add_milestone(
        "Security Enhancements Complete", "2024-04-20", fill_colour="#004E86", font_colour="#004E86"
    )

    task = group.add_task(
        "Infrastructure as Code Standards", "2024-05-01", "2024-07-01", fill_colour="#4472C4", font_colour="white",
    )
    task.add_milestone(
        "IaC Standards Published", "2024-07-15", fill_colour="#004E86", font_colour="#004E86"
    )

    task = group.add_task(
       "Continuous Compliance Monitoring", "2024-08-01", "2024-12-31", fill_colour="#4472C4", font_colour="white",
    )
    task.add_parallel_task(
        "Compliance Audits", "2025-01-15", "2025-03-31", fill_colour="#4472C4", font_colour="white",
    )
    task.add_milestone(
        "Compliance Audits Complete", "2025-04-15", fill_colour="#004E86", font_colour="#004E86"
    )

    # Coding and Development Standards
    group = roadmap.add_group("Coding & Development Standards", fill_colour="#FF5733", font_colour="white")

    task = group.add_task(
        "Coding Standards Development", "2024-01-15", "2024-03-31", fill_colour="#FF5733", font_colour="white",
    )
    task.add_parallel_task(
        "API Standards", "2024-04-01", "2024-06-30", fill_colour="#FF5733", font_colour="white",
    )
    task.add_parallel_task(
        "Serverless Standards", "2024-07-01", "2024-09-30", fill_colour="#FF5733", font_colour="white",
    )
    task.add_milestone(
        "Standards Published", "2024-10-01", fill_colour="#FF3300", font_colour="#FF3300"
    )

    task = group.add_task(
        "Container Standards", "2024-10-01", "2024-12-31", fill_colour="#FF5733", font_colour="white",
    )
    task.add_milestone(
        "Container Standards Implemented", "2025-01-15", fill_colour="#FF3300", font_colour="#FF3300"
    )

    task = group.add_task(
        "Code, Source Code & Dependency Management Standards", "2025-02-01", "2025-04-30", fill_colour="#FF5733", font_colour="white",
    )
    task.add_milestone(
        "Management Standards Implemented", "2025-05-15", fill_colour="#FF3300", font_colour="#FF3300"
    )

    task = group.add_task(
        "Testing and Assurance Standards", "2025-05-01", "2025-07-31", fill_colour="#FF5733", font_colour="white",
    )
    task.add_milestone(
        "Testing Standards Implemented", "2025-08-15", fill_colour="#FF3300", font_colour="#FF3300"
    )

    # Release Engineering
    group = roadmap.add_group("Release Engineering", fill_colour="#33A1FF", font_colour="white")

    task = group.add_task(
        "Release Engineering Standards", "2024-01-15", "2024-03-31", fill_colour="#33A1FF", font_colour="white",
    )
    task.add_parallel_task(
        "Continuous Delivery Enhancements", "2024-04-01", "2024-06-30", fill_colour="#33A1FF", font_colour="white",
    )
    task.add_milestone(
        "Release Standards Published", "2024-07-15", fill_colour="#0059B2", font_colour="#0059B2"
    )

    task = group.add_task(
        "Automated Release Pipeline", "2024-07-01", "2024-09-30", fill_colour="#33A1FF", font_colour="white",
    )
    task.add_parallel_task(
        "Release Pipeline Monitoring", "2024-10-01", "2024-12-31", fill_colour="#33A1FF", font_colour="white",
    )
    task.add_milestone(
        "Automated Release Pipeline Live", "2025-01-15", fill_colour="#0059B2", font_colour="#0059B2"
    )

    roadmap.set_footer("Designed by Group Cloud Engineering")
    roadmap.draw()

    roadmap.save("cloud-engineering-strategy-roadmap.png")

def main():
  cloud_engineering_strategy_road_map_generations()

if __name__ == '__main__':
  main()
