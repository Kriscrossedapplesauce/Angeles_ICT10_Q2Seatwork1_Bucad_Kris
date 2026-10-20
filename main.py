from pyscript import document

def verify_candidate(event):
    """Retrieves input names, checks membership without loops/conditionals, and displays the result."""

    club_members = ["De Leon", "Daniella Guintu", "Kris Bucad", "Maia Rodolfo"]

    fname = document.querySelector("#first_name").value.strip()
    lname = document.querySelector("#last_name").value.strip()

    full_name = f"{fname} {lname}"

    is_member = full_name in club_members

    messages = {
        True: f"Congratulations {full_name}You are now part of the Math club.",
        False: f"Sorry {full_name}, your name is not on the list."
    }

    result_message = messages[is_member]
    document.querySelector("#result-display").innerText = result_message