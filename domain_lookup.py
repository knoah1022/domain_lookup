import whois

def get_domain_info(domain_name):
    try:
        # Query the domain information
        domain = whois.whois(domain_name)

        # Basic check if domain object has a name (which it usually will if lookup was successful)
        if getattr(domain, 'domain_name', None): # Use getattr for the primary check too
            print(f"--- Basic Information for {domain_name} ---")
            print(f'Domain Name(s): {domain.domain_name}') # domain_name can sometimes be a list
            print(f'Registrar: {getattr(domain, "registrar", "Not available")}')
            print(f'WHOIS Server: {getattr(domain, "whois_server", "Not available")}')

            print(f'\n--- Dates ---')
            print(f'Creation Date(s): {getattr(domain, "creation_date", "Not available")}')
            print(f'Expiration Date(s): {getattr(domain, "expiration_date", "Not available")}')
            print(f'Updated Date(s): {getattr(domain, "updated_date", "Not available")}')

            print(f'\n--- Status & Name Servers ---')
            print(f'Status: {getattr(domain, "status", "Not available")}')

            name_servers = getattr(domain, "name_servers", [])
            if name_servers:
                if all(isinstance(ns, str) for ns in name_servers):
                    print(f'Name Servers: {", ".join(name_servers)}')
                else:
                    # Handle cases where name_servers might be structured differently (e.g., objects)
                    print(f'Name Servers: {name_servers}') # Print as is if not simple list of strings
            else:
                print(f'Name Servers: Not available')

            print(f'\n--- Registrant Information (often limited by privacy) ---')
            print(f'Registrant Organization: {getattr(domain, "org", "Not available")}')
            print(f'Registrant Country: {getattr(domain, "country", "Not available")}')
            # Other common registrant fields: name, address, city, state, zipcode, email
            # Example: print(f'Registrant Email: {getattr(domain, "email", "Not available")}') # Usually redacted

        else:
            # This handles cases where the domain might not exist or
            # the whois lookup returns an empty or minimal result.
            print(f"No detailed WHOIS information found for {domain_name}.")
            # You can print the raw domain object to see everything it contains:
            # print(f"Raw WHOIS object attributes: {dir(domain)}")
            # print(f"Raw WHOIS text: {domain.text}") # If you want to see the raw text

    except Exception as e:
        # This is a very general error handler.
        print(f'An error occurred while fetching information for {domain_name}: {e}')
        # For debugging, you might want to see the type of error:
        # print(f'Error type: {type(e).__name__}')

if __name__ == '__main__':
    domain_input = input('Enter a domain name (e.g., example.com): ').strip().lower()
    if domain_input: # Simple check for empty input
        get_domain_info(domain_input)
    else:
        print("No domain name entered.")