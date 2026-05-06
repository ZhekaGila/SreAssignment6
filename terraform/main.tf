provider "aws" {
  region = var.region
}

resource "aws_security_group" "sre_sg" {
  name = "sre-sg"

  ingress {
    from_port   = 3000
    to_port     = 3000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 9090
    to_port     = 9090
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["92.46.171.180/32"] # твой IP
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "sre_vm" {
  ami           = var.ami
  instance_type = "t3.micro"

  vpc_security_group_ids = [aws_security_group.sre_sg.id]
  key_name               = var.key_name

  tags = {
    Name = "sre-assignment"
  }
}
