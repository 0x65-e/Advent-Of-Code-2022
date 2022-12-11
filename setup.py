import os
import requests
import sys

def main():
    # Validate commandline parameters
    if (len(sys.argv) != 2):
        print("Usage: {} [NUM]".format(sys.argv[0]), file=sys.stderr)
        exit(1)
    try:
        day_number = int(sys.argv[1])
    except ValueError:
        print("Usage: {} [NUM]".format(sys.argv[0]), file=sys.stderr)
        exit(1)
    
    # Read the session cookie from a local file
    with open("SESSION") as f:
        session_cookie = f.readline()
    
    # Request the input
    with requests.Session() as s:
        req = s.get("https://adventofcode.com/2022/day/{}/input".format(day_number), cookies={"session": session_cookie})
        if (req.status_code != 200):
            print("Error requesting input:", file=sys.stderr)
            print(req.text)
            exit(1)
    
    # Write the input to a file
    try:
        os.mkdir("inputs")
    except OSError:
        pass

    with open(os.path.join("inputs", "input{:02}.txt".format(day_number)), 'w') as input_file:
        input_file.write(req.text)

    # Touch the solution file
    solution_file_path = os.path.join("python3", "solution{:02}.py".format(day_number))
    if os.path.exists(solution_file_path):
        # Don't overwrite an existing solution
        print("Solution file already exists. Skipping.")
    else:
        # Create a solution file from a template
        with open(os.path.join("python3", "template.py")) as template_file:
            template = template_file.read()
        
        with open(solution_file_path, 'w') as soln_file:
            soln_file.write(template.replace("00", "{:02}".format(day_number)))
    

if __name__ == "__main__":
    main()