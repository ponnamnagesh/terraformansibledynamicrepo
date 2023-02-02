import json
import requests

def parse_terraform_backend(file_path):
    with open(file_path) as f:
        backend_config = json.load(f)

    # Extract the relevant information about EC2 instances and other services
    ec2_instances = backend_config["resources"]["aws_instance"]
    other_services = backend_config["resources"]["<other_service_name>"]

    # Parse the information to extract IP addresses
    ec2_ips = [instance["primary"]["attributes"]["private_ip"] for instance in ec2_instances]
    other_service_ips = [service["primary"]["attributes"]["<attribute_containing_ip>"] for service in other_services]

    # Output the IP addresses in a format that Ansible can use
    output = {
        "ec2_ips": ec2_ips,
        "other_service_ips": other_service_ips
    }

    return output

def write_inventory_file(inventory_file_path, inventory_data):
    with open(inventory_file_path, "w") as f:
        f.write("[ec2_instances]\n")
        for ip in inventory_data["ec2_ips"]:
            f.write(f"{ip}\n")

        f.write("\n[other_services]\n")
        for ip in inventory_data["other_service_ips"]:
            f.write(f"{ip}\n")

def deploy_artifact(artifact_url, target_dir):
    response = requests.get(artifact_url)

    with open(f"{target_dir}/<artifact_file>", "wb") as f:
        f.write(response.content)

if __name__ == "__main__":
    terraform_backend_file = "<path_to_terraform_backend_file>"
    output = parse_terraform_backend(terraform_backend_file)
    inventory_file = "<path_to_inventory_file>"
    write_inventory_file(inventory_file, output)

    artifact_url = "<artifactory_url>/<artifact_path>"
    target_dir = "<target_directory>"
    deploy_artifact(artifact_url, target_dir)

    print("Inventory file created and artifact deployed successfully!")
