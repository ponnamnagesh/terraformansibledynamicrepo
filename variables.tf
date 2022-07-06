variable "aws_ami_id" {
  ## Amazon Linux 2 AMI (HVM)
  ##default = "ami-02f26adf094f51167"
  default = "ami-05803413c51f242b7"

  ## "ami-0cd31be676780afa7"
}

variable "ssh_key_pair" {
  default = "~/.ssh/id_rsa"
}

variable "ssh_key_pair_pub" {
  default = "~/.ssh/id_rsa.pub"
}

variable "ansible_node_count" {
  default = 2
}
