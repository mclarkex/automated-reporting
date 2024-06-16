"""
Generates a visualised roadmap of for the Azure Cloud Foundations Product. 

Colours codes can be found:
 - Documentation: Writing Documents - https://landg.atlassian.net/wiki/spaces/CED/pages/6200328487/Documentation+Writing+Documents
 - Core Blue:#0076D6
 - Core Green:#028844
 - Core Yellow:#FFD500
 - Core Red:#E22922
 - Charcoal:#333333

"""

import os 

current_dir = os.getcwd()
os.chdir("./roadmaps/")


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
        start = "2024-01-01",
        number_of_items = 16,
        show_generic_dates=False,
        year_fill_colour="#008AD7",
        year_font_colour="white",
        item_fill_colour="#008AD7",
        item_font_colour="white",
    )

    #Planning 
    """This workstream relates to planning activities 
        -Architecture
        -Resource Planning 
    """    
    group = roadmap.add_group("Planning", fill_colour="#028844", font_colour="white")
    
    task = group.add_task(
       "Tranfer Azure CF", "2024-01-01","2024-03-15",  fill_colour="#028844", font_colour="white"
    )
    task.add_parallel_task(
       "Azure GAP Analysis", "2024-03-18", "2024-05-30", fill_colour="#028844", font_colour="white"
    )

    task = group.add_task(
       "Azure Resource Profile", "2024-03-01","2024-06-15",  fill_colour="#028844", font_colour="white"
    )

    task.add_milestone(
        "SRE Team Onboarded", "2024-09-20", fill_colour="#005629", font_colour="#005629"
    )


    task = group.add_task(
       "Network Design Review", "2024-04-01","2024-06-20",  fill_colour="#028844", font_colour="white"
    )

    task.add_parallel_task(
        "Network Firewalls",
        "2024-06-21",
        "2024-08-30",
        fill_colour="#028844",
        font_colour="white",
    )

    task.add_milestone(
        "RfP Awarded", "2024-05-20", fill_colour="#005629", font_colour="#005629"
    )

    #Strategy
    group = roadmap.add_group("Strategy & Governance", fill_colour="#FFD500", font_colour="black")
    task = group.add_task(
        "Internal Cloud Analysis",
        "2024-02-01",
        "2024-04-20",
        fill_colour="#FFD500",
        font_colour="black",
    )
    task.add_milestone(
        "Audit HR1.1 Due", "2024-05-15", fill_colour="#DD9C00", font_colour="#DD9C00"
    )

    task.add_milestone(
        "Audit HR1.2 Due", "2024-09-15", fill_colour="#DD9C00", font_colour="#DD9C00"
    )

    task.add_milestone(
        "Audit HR1.3 Due", "2024-11-15", fill_colour="#DD9C00", font_colour="#DD9C00"
    )

    task.add_milestone(
        "Audit HR1.4 Due", "2024-12-30", fill_colour="#DD9C00", font_colour="#DD9C00"
    )

    task = group.add_task(
        "FinOps and Financial Reporting",
        "2024-01-01",
        "2024-11-20",
        fill_colour="#FFD500",
        font_colour="black",
    )

    task = group.add_task(
        "New Cloud Operating Model",
        "2024-06-01",
        "2024-09-20",
        fill_colour="#FFD500",
        font_colour="black",
    )


    #Service Development
    group = roadmap.add_group(
        "Product Development", fill_colour="#E22922", font_colour="white"
    )

    task = group.add_task(
       "GitHub Integration",
       "2024-02-10",
       "2024-04-10",
        fill_colour="#E22922",
        font_colour="white",
    )

    parallel_task = task.add_parallel_task(
        "GitHub Backup",
        "2024-04-05",
        "2024-05-30",
        fill_colour="#E22922",
        font_colour="white",
    )

    parallel_task = task.add_parallel_task(
        "GitHub Migrations",
        "2024-05-30",
        "2024-07-25",
        fill_colour="#E22922",
        font_colour="white",
    )

    parallel_task.add_milestone(
        "Service Readiness: GitHub", "2024-07-30", fill_colour="#A81815", font_colour="#A81815"
    )

    task = group.add_task(
       "Tranfer: Supplier to Group Technology",
       "2024-10-10",
       "2025-04-10",
        fill_colour="#E22922",
        font_colour="white",
    )

    task = group.add_task(
       "Documentation Improvements",
       "2024-03-15",
       "2024-08-10",
        fill_colour="#E22922",
        font_colour="white",
    )

    task = group.add_task(
       "Service Now Form Improvements",
       "2024-03-15",
       "2024-08-10",
        fill_colour="#E22922",
        font_colour="white",
    )

    parallel_task = task.add_parallel_task(
        "Seamless Account Vending",
        "2024-08-10",
        "2024-12-30",
        fill_colour="#E22922",
        font_colour="white",
    )

    task = group.add_task(
        "Preventative Guardrails",
        "2024-01-26",
        "2025-02-16",
        fill_colour="#E22922",
        font_colour="white",
    )

    task = group.add_task(
        "Product Roadmap",
        "2024-04-26",
        "2024-09-16",
        fill_colour="#E22922",
        font_colour="white",
    )
  
    parallel_task.add_milestone(
        "Azure CF v1.0", "2024-10-10", fill_colour="#A81815", font_colour="#A81815"
    )
    parallel_task.add_milestone(
        "Azure v2.0", "2025-04-10", fill_colour="#A81815", font_colour="#A81815"
    )

    #Platform 
    group = roadmap.add_group("Platform & Engineering", fill_colour="#333333", font_colour="white")

    task = group.add_task(
       "Terraform Enterprise Integration",
       "2024-03-15",
       "2024-08-10",
        fill_colour="#333333",
        font_colour="white",
    )

    #Operations
    group = roadmap.add_group(
        "Operations",
        fill_colour="#4472C4",
        font_colour="white",
    )

    task = group.add_task(
        "CSMP Integration",
        "2024-05-30",
        "2024-09-29",
        fill_colour="#4472C4",
        font_colour="white",
    )

    task = group.add_task(
        "Lighthouse Control Framework",
        "2024-03-30",
        "2024-09-29",
        fill_colour="#4472C4",
        font_colour="white",
    )
    
    
    task = group.add_task(
        "Splunk Integration",
        "2024-05-15",
        "2024-07-29",
        fill_colour="#4472C4",
        font_colour="white",
    )

    task = group.add_task(
        "Sailpoint Integration",
        "2024-05-15",
        "2024-07-29",
        fill_colour="#4472C4",
        font_colour="white",
    )

    parallel_task = task.add_parallel_task(
        "RBAC Design",
        "2024-07-29",
        "2024-09-15",
        fill_colour="#4472C4",
        font_colour="white",
    )

    task = group.add_task(
        "Grafana Integration",
        "2024-06-15",
        "2024-08-29",
        fill_colour="#4472C4",
        font_colour="white",
    )

    parallel_task = task.add_parallel_task(
        "Monitoring Dashboards",
        "2024-09-01",
        "2024-11-15",
        fill_colour="#4472C4",
        font_colour="white",
    )

    parallel_task = task.add_parallel_task(
        "Oncall and incident management",
        "2024-11-17",
        "2025-03-15",
        fill_colour="#4472C4",
        font_colour="white",
    )

    parallel_task.add_milestone(
        "Service Readiness:Grafana", "2024-08-25", fill_colour="#004E86", font_colour="#004E86"
    )
    
    roadmap.set_footer("Designed by Group Cloud Engineering")
    roadmap.draw()

    roadmap.save("azure-cloud-foundations-roadmap.png")

def main():
  azure_cloud_foundations_road_map_generations()


if __name__ == '__main__':
  main()