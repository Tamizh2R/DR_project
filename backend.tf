terraform {
  backend "s3" {
    bucket         = "dr-terraform-state1"
    key            = "terraform.tfstate"
    region         = "ap-southeast-2"
    encrypt        = true
  }
}

