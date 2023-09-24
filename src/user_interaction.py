def get_threshold():
    try:
        threshold = float(input("Enter the download speed threshold (in Mbps) that you consider too low: "))
        return threshold
    except ValueError:
        print("Please enter a valid number.")
        return get_threshold()


def select_isp():
    isps = {
        "AT&T": "@ATT",
        "Comcast (Xfinity)": ["@comcast", "@Xfinity"],
        "Verizon": "@verizon",
        "Spectrum (Charter Communications)": "@GetSpectrum",
        "Cox Communications": "@CoxComm",
        "CenturyLink (now known as Lumen Technologies)": ["@CenturyLink", "@LumenTechCo"],
        "Frontier Communications": "@FrontierCorp",
        "T-Mobile Home Internet": "@TMobile",
        "Mediacom": "@MediacomCable",
        "Windstream": "@Windstream",
    }

    print("Select your ISP:")
    for index, isp in enumerate(isps.keys(), start=1):
        print(f"{index}. {isp}")

    try:
        choice = int(input())
        if 1 <= choice <= len(isps):
            selected_isp = list(isps.keys())[choice - 1]
            return isps[selected_isp]
        else:
            print("Invalid choice. Please select a number from the list.")
            return select_isp()
    except ValueError:
        print("Please enter a valid number.")
        return select_isp()
