import settings
import os

def main():
  # The environment variable can be fetched as follows
  mySecret = os.getenv("SECRET")
  print(mySecret)

if __name__ == "__main__":
  main()
