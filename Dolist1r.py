import argparse  # Thư viện để xử lý đối số dòng lệnh
import dns.resolver  # Thư viện để thực hiện các truy vấn DNS
import dns.exception  # Để xử lý lỗi từ dnspython


def check_subdomain_exists(subdomain):
    """
    Kiểm tra xem một tên miền phụ có tồn tại bằng cách truy vấn DNS hay không.
    """
    try:
        # Cố gắng phân giải bản ghi 'A' (IPv4) cho tên miền phụ.
        answers = dns.resolver.resolve(subdomain, 'A')
        return True
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.NoNameservers, dns.exception.Timeout):
        return False
    except Exception as e:
        return False


def main():
    print(r"""
    ██████╗  ██████╗ ██╗     ██████╗ ██╗     ████████╗██╗██████╗
    ██╔══██╗██╔═══██╗██║     ██╔══██╗██║     ╚══██╔══╝██║██╔══██╗
    ██║  ██║██║   ██║██║     ██║  ██║██║        ██║   ██║██████╔╝
    ██║  ██║██║   ██║██║     ██║  ██║██║        ██║   ██║██╔══██╗
    ██████╔╝╚██████╔╝███████╗██████╔╝███████╗   ██║   ██║██║  ██║
    ╚═════╝  ╚═════╝ ╚══════╝╚═════╝ ╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═╝
        """)
    print("        Một công cụ liệt kê tên miền phụ đơn giản bằng Brute-Force")
    print("                      Phiên bản: 1.0 (Dolist1r)")
    print("----------------------------------------------------------------------")
    parser = argparse.ArgumentParser(
        description="Một công cụ liệt kê tên miền phụ đơn giản bằng bruteforce."
    )

    # Định nghĩa các đối số.
    # -d hoặc --domain: Tên miền mục tiêu.
    parser.add_argument(
        '-d', '--domain',
        type=str,
        required=True,
        help="Tên miền chính để liệt kê tên miền phụ (ví dụ: example.com)."
    )

    # -w hoặc --wordlist: Đường dẫn đến tệp wordlist.
    parser.add_argument(
        '-w', '--wordlist',
        type=str,
        required=True,
        help="Đường dẫn đến tệp văn bản chứa danh sách các tiền tố tên miền phụ."
    )

    args = parser.parse_args()  # Phân tích các đối số được cung cấp.

    domain_target = args.domain
    wordlist_path = args.wordlist

    print(f"[*] Bắt đầu liệt kê tên miền phụ cho: {domain_target}")
    print(f"[*] Sử dụng wordlist từ: {wordlist_path}")

    found_subdomains = []

    try:
        # Mở và đọc tệp wordlist.
        with open(wordlist_path, 'r') as f:
            for line in f:
                prefix = line.strip()
                if not prefix:
                    continue

                # Tạo tên miền phụ đầy đủ.
                subdomain_to_check = f"{prefix}.{domain_target}"

                print(f"[?] Đang kiểm tra: {subdomain_to_check}")

                # Kiểm tra sự tồn tại của tên miền phụ.
                if check_subdomain_exists(subdomain_to_check):
                    print(f"[+] Tìm thấy tên miền phụ: {subdomain_to_check}")
                    found_subdomains.append(subdomain_to_check)

    except FileNotFoundError:
        print(f"[!] Lỗi: Không tìm thấy tệp wordlist tại '{wordlist_path}'. Vui lòng kiểm tra lại đường dẫn.")
        return
    except Exception as e:
        print(f"[!] Đã xảy ra lỗi khi đọc wordlist hoặc trong quá trình quét: {e}")
        return

    print("\n[--- Quá trình quét hoàn tất ---]")
    if found_subdomains:
        print("[*] Các tên miền phụ đã tìm thấy:")
        for subdomain in found_subdomains:
            print(f"- {subdomain}")

        output_file_name = f"subdomains_{domain_target.replace('.', '_')}.txt"
        with open(output_file_name, 'w') as out_f:
            for subdomain in found_subdomains:
                out_f.write(subdomain + '\n')
        print(f"[*] Kết quả đã được lưu vào: {output_file_name}")
    else:
        print("[!] Không tìm thấy tên miền phụ nào.")


if __name__ == "__main__":
    main()