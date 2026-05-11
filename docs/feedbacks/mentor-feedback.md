Grammar-based Greybox Fuzzing for DBMS Vulnerability Detection 

Nội dung 1. Attack-pattern based grammar construction
Phân tích các CVEs liên quan DBMS và rút ra các patterns. Từ đó tạo văn phạm, tức các luật sản xuất theo các patterns. Cung cấp văn phạm cho Nautilus.
Core grammar: v1
Extended grammar: v2
CVE2grammar


Nội dung 2: Reinforcement Learning 
RL on core grammar
RL on extended grammar






Attack-pattern based grammar có khả năng phát hiện lại các CVE cũ, hoặc các lỗ hổng tương tự CVE cũ.
Nhưng nó khó phát hiện 0-day. 
Nghiên cứu cải tiến để phát hiện 0-day theo các hướng sau:

1. Tổ hợp chéo các mẫu tấn công (Cross-Pollination of Patterns)
Thay vì dùng mẫu tấn công một cách nguyên bản, hãy cho phép văn phạm EBNF kết hợp chéo các tính năng ít liên quan lại với nhau. Các lỗi 0-day thường nằm ở sự giao thoa giữa các module ít được kiểm thử cùng nhau.
Ví dụ: Một CVE cũ khai thác lỗi tràn bộ đệm trong hàm xử lý chuỗi JSON, một CVE khác khai thác lỗi logic trong Window Functions. Cải tiến ở đây là định nghĩa văn phạm sao cho Nautilus có thể nhúng cụm tấn công JSON vào bên trong mệnh đề OVER() của một Window Function.
2. Tăng cường đột biến cấu trúc sâu (Deep Structural Generation)
0-day thường trốn ở những cây cú pháp (AST) có độ sâu hoặc độ rộng bất thường mà các bài test của lập trình viên không bao giờ chạm tới.
Giải pháp: Trong EBNF, cần thiết kế các luật sản xuất có tính đệ quy cao (Recursive Rules). Ví dụ: cho phép lồng ghép SELECT bên trong SELECT hàng chục lần, hoặc tạo ra các chuỗi JOIN hoặc UNION khổng lồ. Nautilus hỗ trợ rất tốt việc sinh ra các cây dẫn xuất sâu nếu văn phạm cho phép.
