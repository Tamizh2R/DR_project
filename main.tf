resource "aws_instance" "my_ec2" {
  ami = "ami-0a2e29e3b4fc39212"
  instance_type = "t2.micro"
  tags = {
    Name = "DR_PROJECT_EC2"
  }
}
