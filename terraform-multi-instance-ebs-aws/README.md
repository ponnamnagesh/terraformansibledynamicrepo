# terraform
terraform stuffs


In the below variables, if we choose this one #default = ["us-east-1a", "us-east-1b", "us-east-1c"] and execute terraform, then we will get error.

After the error, if choose this one default = ["us-east-1b", "us-east-1a", "us-east-1c"], then it will be executed without error.

variable "azs" {
 type = list
  default = ["us-east-1b", "us-east-1a", "us-east-1c"]
  #default = ["us-east-1a", "us-east-1b", "us-east-1c"]
}_
