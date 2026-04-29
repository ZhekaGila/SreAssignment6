variable "project_name" {
  description = "Project name"
  type        = string
  default     = "sre_assignment"
}

variable "region" {
  default = "us-east-1"
}

variable "instance_type" {
  default = "t2.micro"
}

variable "ami" {
  description = "AMI ID"
}

variable "key_name" {
  description = "SSH key name"
}