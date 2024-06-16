import os

current_dir = os.getcwd()
os.chdir("./automated-reporting/roadmaps/")

def azure_test_road_map_generations():

    from roadmapper.roadmap import Roadmap
    from roadmapper.timelinemode import TimelineMode

    roadmap = Roadmap(
            1400, 1000, auto_height=True, show_marker=True
        )
    roadmap.set_title("Cloud Test ROADMAP 2024")
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

    # Test Planning
    group = roadmap.add_group("Test Planning", fill_colour="#028844", font_colour="white")
    
    task = group.add_task(
       "Define Test Strategy", "2024-01-01","2024-02-28",  fill_colour="#028844", font_colour="white"
    )
    task.add_parallel_task(
       "Identify Test Cases", "2024-03-01", "2024-04-30", fill_colour="#028844", font_colour="white"
    )

    task = group.add_task(
       "Test Environment Setup", "2024-05-01","2024-07-31",  fill_colour="#028844", font_colour="white"
    )
    task.add_milestone(
        "Environment Ready", "2024-08-15", fill_colour="#005629", font_colour="#005629"
    )

    # Test Execution
    group = roadmap.add_group("Test Execution", fill_colour="#FFD500", font_colour="black")
    task = group.add_task(
        "Functional Testing", "2024-02-01", "2024-03-15", fill_colour="#FFD500", font_colour="black",
    )
    task.add_milestone(
        "Functional Testing Complete", "2024-03-20", fill_colour="#DD9C00", font_colour="#DD9C00"
    )

    task = group.add_task(
        "Integration Testing", "2024-03-15", "2024-05-30", fill_colour="#FFD500", font_colour="black",
    )
    task.add_milestone(
        "Integration Testing Complete", "2024-06-01", fill_colour="#DD9C00", font_colour="#DD9C00"
    )

    task = group.add_task(
        "System Testing", "2024-06-01", "2024-08-15", fill_colour="#FFD500", font_colour="black",
    )
    task.add_milestone(
        "System Testing Complete", "2024-08-20", fill_colour="#DD9C00", font_colour="#DD9C00"
    )

    # Performance Testing
    group = roadmap.add_group("Performance Testing", fill_colour="#E22922", font_colour="white")

    task = group.add_task(
       "Load Testing", "2024-04-10", "2024-05-15", fill_colour="#E22922", font_colour="white",
    )
    task.add_parallel_task(
        "Stress Testing", "2024-05-20", "2024-06-30", fill_colour="#E22922", font_colour="white",
    )
    task.add_milestone(
        "Performance Testing Complete", "2024-07-01", fill_colour="#A81815", font_colour="#A81815"
    )

    task = group.add_task(
       "Scalability Testing", "2024-06-01", "2024-07-31", fill_colour="#E22922", font_colour="white",
    )

    # User Acceptance Testing (UAT)
    group = roadmap.add_group("User Acceptance Testing (UAT)", fill_colour="#333333", font_colour="white")

    task = group.add_task(
       "UAT Planning", "2024-07-01", "2024-08-01", fill_colour="#333333", font_colour="white",
    )
    task.add_parallel_task(
        "UAT Execution", "2024-08-05", "2024-09-30", fill_colour="#333333", font_colour="white",
    )
    task.add_milestone(
        "UAT Complete", "2024-10-01", fill_colour="#555555", font_colour="#555555"
    )

    # Test Automation
    group = roadmap.add_group("Test Automation", fill_colour="#4472C4", font_colour="white")

    task = group.add_task(
        "Develop Test Scripts", "2024-01-15", "2024-05-15", fill_colour="#4472C4", font_colour="white",
    )
    task.add_milestone(
        "Test Scripts Ready", "2024-05-20", fill_colour="#004E86", font_colour="#004E86"
    )

    task = group.add_task(
        "Implement CI/CD Integration", "2024-05-20", "2024-08-20", fill_colour="#4472C4", font_colour="white",
    )
    task.add_milestone(
        "CI/CD Integration Complete", "2024-08-25", fill_colour="#004E86", font_colour="#004E86"
    )

    roadmap.set_footer("Designed by Group Cloud Engineering")
    roadmap.draw()

    roadmap.save("azure-test-roadmap.png")

def main():
  azure_test_road_map_generations()

if __name__ == '__main__':
  main()
