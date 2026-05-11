# Kiểm Toán Dự Án Nghiên Cứu: RL-Nautilus

**Ngày:** 24-04-2026
**Người kiểm toán:** Claude (Cố vấn Nghiên cứu Cấp cao)
**Nhánh:** phase-2
**Phạm vi:** Kiểm toán toàn diện dự án, đối chiếu với khung nghiên cứu chuẩn cho bài báo khoa học

---

## 1. Tóm Tắt Dự Án

RL-Nautilus là một fuzzer dựa trên ngữ pháp và hướng dẫn bởi coverage (fork từ Nautilus 2.0, viết bằng Rust), được tăng cường bằng lấy mẫu ngữ pháp có trọng số và một agent học tăng cường DQN để lựa chọn chiến lược đột biến thích ứng, nhắm vào việc tái phát hiện tự động các CVE đã biết trong SQLite. Dự án fuzz 4 phiên bản SQLite chứa CVE (3.30.1, 3.31.1, 3.32.0, 3.32.2) và bao gồm một pipeline phụ (`cve2grammar`) thu thập các báo cáo lỗi DBMS đã biết, tổng quát hóa chúng qua LLM thành các quy tắc ngữ pháp, và render thành ngữ pháp Python tương thích Nautilus.

---

## 2. Bảng Trạng Thái Theo Khung Nghiên Cứu

| Giai đoạn | Trạng thái | Những gì đã có | Những gì còn thiếu |
|-----------|-----------|----------------|-------------------|
| **1 — Câu hỏi Nghiên cứu** | Một phần | Giả thuyết ngầm: việc lựa chọn chiến lược đột biến hướng dẫn bởi RL cải thiện phát hiện CVE so với lấy mẫu có trọng số tĩnh/đồng đều. Miền mục tiêu rõ ràng (fuzzing SQLite). | **Không có phát biểu giả thuyết chính thức.** Ablation Phase 2 đã *bác bỏ* giả thuyết trung gian ("chất lượng ngữ pháp chắt lọc thắng độ rộng từ vựng"). Giả thuyết RL chưa được kiểm chứng. Không có phát biểu đóng góp rõ ràng phù hợp cho abstract bài báo. |
| **2 — Tài liệu tham khảo / Baseline** | Yếu | Bài báo Nautilus NDSS'19 được tham chiếu. AFL++ làm fork server baseline. So sánh thủ công với lấy mẫu đồng đều. | **Không có tổng quan tài liệu có hệ thống.** Thiếu so sánh với: AFL++ đơn thuần (không ngữ pháp), Superion, Grimoire, Squirrel (fuzzer nhận biết SQL), LMQL, FuzzGPT, ChatFuzz, các bài báo RL-fuzz khác (NEUZZ, MTFuzz, FuzzRL). Không có tài liệu tổng quan nghiên cứu. |
| **3 — Thiết kế Thí nghiệm** | Trung bình | Ablation E2 (4 biến thể x 2 seed x 15 phút) với đếm root-cause bằng stack_dedup. Chấm điểm fidelity (A3) với chữ ký CVE dựa trên regex. Thu thập coverage (A2). | **N=2 mỗi biến thể (quá thấp cho các khẳng định thống kê).** Không có kiểm định thống kê. Không có khái niệm train/val/test split (đây là fuzzing, không phải ML — nhưng agent RL *là* ML và không có giao thức đánh giá). Không có quét ngân sách thời gian. Chỉ 1 trong 4 phiên bản mục tiêu được thử nghiệm. Khung thời gian 15 phút có thể quá ngắn. Không có ablation trên siêu tham số RL. |
| **4 — Thực thi & Kết quả** | Trung bình | Một ablation E2 hoàn chỉnh trên sqlite-3.31.1 với phân tích trung thực. Delta fidelity v1/v2 được ghi nhận. Mã DQN hoàn chỉnh và đã test tích hợp (dqn_test.rs). | **RL chưa bao giờ được chạy trong chiến dịch fuzzing thực** (`rl_enabled: false` trong tất cả config). Không có kết quả RL nào. Không có theo dõi thí nghiệm (không wandb/mlflow). Không có seed đã lưu (Nautilus không có kiểm soát RNG seed). Coverage.json đôi khi trích xuất thất bại. |
| **5 — Viết bài & Nộp bài** | Sớm | README tốt, tài liệu kiến trúc, báo cáo ablation, danh sách CVE. Sơ đồ Mermaid. CLAUDE.md kỹ lưỡng. | **Không có bản thảo bài báo.** Không có LaTeX. Không có abstract. Không có hình/biểu đồ. Không có bảng thống kê phù hợp cho bài báo. Báo cáo ablation trung thực nhưng đọc như ghi chú nội bộ, không phải một phần bài báo. |

---

## 3. Top 3 Khoảng Trống Nghiêm Trọng

### Khoảng trống 1: Thành phần RL chưa bao giờ được đánh giá

Toàn bộ tiêu đề luận văn là "Fuzzer Dựa trên Ngữ pháp với **RL** cho Phát hiện CVE" nhưng `rl_enabled` chưa bao giờ được đặt thành `true` trong một chiến dịch thực. Agent DQN biên dịch được và pass unit test với dữ liệu ngẫu nhiên, nhưng không có kết quả nào cho thấy nó có giúp ích, gây hại, hay trung tính. **Đây là đóng góp cốt lõi và nó hoàn toàn chưa được kiểm chứng.** Cho đến khi bạn chạy các chiến dịch RL và so sánh chúng với baseline, bạn không có bài báo.

### Khoảng trống 2: Thiếu độ chặt chẽ thống kê (N=2, không có kiểm định ý nghĩa)

Ablation E2 sử dụng 2 lần chạy mỗi biến thể mà không có kiểm soát RNG seed. Điều này được thừa nhận rõ ràng trong báo cáo ("nên đọc như sàn của độ biến thiên giữa các lần chạy, không phải CI thực") nhưng 2 điểm dữ liệu không thể hỗ trợ bất kỳ khẳng định thống kê nào. Để viết bài báo, bạn cần tối thiểu N=10 mỗi biến thể với kiểm định Mann-Whitney U hoặc kiểm định phi tham số tương tự, cộng với khoảng tin cậy cho TTFC và số lượng RC.

### Khoảng trống 3: Không có bản thảo bài báo hoặc giả thuyết chính thức

Không có tài liệu LaTeX, không có abstract, không có phát biểu vấn đề chính thức. Báo cáo ablation trung thực về mặt trí tuệ nhưng các phát hiện là tiêu cực (ngữ pháp chắt lọc tệ hơn thư viện đầy đủ, trọng số không quan trọng ở 15 phút). Nếu không có giả thuyết được tái định khung rằng agent RL khắc phục hạn chế của trọng số tĩnh, không có khẳng định luận văn tích cực nào để bảo vệ.

---

## 4. Kế Hoạch Thí Nghiệm Đề Xuất

| # | Thí nghiệm | Mục tiêu | Baseline | Dữ liệu/Mục tiêu | Chỉ số | Kết quả Dự kiến |
|---|-----------|----------|----------|-------------------|--------|----------------|
| **E1** | **RL vs Mặc định** (thí nghiệm cốt lõi) | Kiểm tra liệu lựa chọn đột biến hướng dẫn bởi DQN có tìm nhiều root cause duy nhất hơn hoặc TTFC nhanh hơn so với Nautilus mặc định | DefaultPolicy (rl_enabled=false) | sqlite-3.31.1, chạy 1 giờ, N=10 mỗi nhánh | Root cause duy nhất (RC), TTFC, đường cong tăng trưởng coverage, tổng crash | RL tìm cùng hoặc +1-2 RC nhanh hơn, hoặc không khác biệt (kết quả null — vẫn có thể xuất bản như phát hiện thực nghiệm) |
| **E2** | **RL vs Chính sách Ngẫu nhiên** | Tách biệt "lựa chọn một chiến lược" khỏi "lựa chọn đã học" — DQN có học được gì không hay lựa chọn hành động ngẫu nhiên là tương đương? | UniformRandomPolicy (chọn ngẫu nhiên 1 trong 5 chiến lược mỗi vòng) | sqlite-3.31.1, 1h, N=10 | RC, TTFC, phân bố hành động theo thời gian, hội tụ Q-value | RL nên cho thấy sự thay đổi phân bố hành động và phân biệt Q-value; nếu không, kiến trúc DQN cần xem xét lại |
| **E3** | **Quét ngân sách thời gian** | Kiểm tra liệu lợi thế ngữ pháp có trọng số / RL có xuất hiện ở khung thời gian dài hơn (15 phút quá ngắn cho chuyển đổi fidelity-thành-crash) | patterns_uniform @ 15m, 1h, 4h | sqlite-3.31.1, N=5 mỗi mốc thời gian | Trần RC vs đường cong thời gian thực | Ngân sách dài hơn nên cho thấy sự phân kỳ nếu hiệu ứng trọng số/RL tồn tại |
| **E4** | **Tổng quát hóa xuyên phiên bản** | Phương pháp ngữ pháp + RL có chuyển giao được qua các phiên bản SQLite không, hay bị overfit vào 3.31.1? | Cùng config chạy trên 3.30.1, 3.32.0, 3.32.2 | Cả 4 phiên bản CVE, 1h, N=5 | RC mỗi phiên bản, phát hiện crash đặc thù CVE | Ít nhất 2/4 phiên bản nên tạo ra crash khớp CVE |
| **E5** | **Độ nhạy siêu tham số RL** | Siêu tham số nào quan trọng? (epsilon decay, replay size, train interval) | Config DQN mặc định | sqlite-3.31.1, 1h, N=5 mỗi config | RC, hội tụ loss, entropy hành động | Xác định siêu tham số nào có tác động đo được — cần cho phần tái tạo |
| **E6** | **Ablation từ vựng ngữ pháp** (mở rộng E2) | Thêm `sqlite_generated.py` đầy đủ (42 quy tắc cve2grammar kết hợp với patterns) làm biến thể thứ 5 | patterns, uniform, attack_v1, attack_v2, generated_composed | sqlite-3.31.1, 1h, N=5 | RC, fidelity, coverage | Ngữ pháp generated nên bằng hoặc vượt trần RC của patterns nếu giả thuyết từ-vựng-là-vua đúng |

---

## 5. Kế Hoạch Hành Động 2 Tuần

### Tuần 1: Làm cho RL chạy được + kết quả đầu tiên

| Ngày | Nhiệm vụ | Sản phẩm |
|------|----------|----------|
| **Ngày 1** | Sửa pipeline `rl_enabled: true` end-to-end. Chạy smoke test 15 phút với DQN bật. Xác minh `rl_metrics.csv` được ghi và chứa dữ liệu hợp lý. | Smoke test pass, rl_metrics.csv được tạo |
| **Ngày 2** | Kết hợp `sqlite_generated.py` + `sqlite_patterns.py` thành một ngữ pháp tự chứa (bước tiếp theo đã biết trong CLAUDE.md). Test nó load mà không panic "Broken Grammar". | `grammars/sqlite_composed.py` hoạt động |
| **Ngày 3** | Viết `UniformRandomPolicy` (đơn giản: chiến lược ngẫu nhiên mỗi vòng, không học) cho baseline E2. Viết `scripts/run_rl_ablation.sh` chạy 3 nhánh: Default, DQN, Random. | Script ablation mới, thiết kế 3 nhánh |
| **Ngày 4-5** | Chạy pilot E1: chạy 1 giờ, N=3 mỗi nhánh (Default, DQN, Random) trên sqlite-3.31.1. Phân tích rl_metrics.csv: epsilon có giảm không? Q-value có phân biệt không? Có crash nào không? | Kết quả RL đầu tiên, dù là sơ bộ |

### Tuần 2: Độ chặt chẽ thống kê + khung bài báo

| Ngày | Nhiệm vụ | Sản phẩm |
|------|----------|----------|
| **Ngày 6-7** | Mở rộng E1 lên N=10 mỗi nhánh (có thể chạy batch qua đêm). Viết script phân tích tính Mann-Whitney U trên số lượng RC và bootstrap CI trên TTFC. | `scripts/analyze_rl.py` với kiểm định thống kê |
| **Ngày 8** | Chạy E4 xuyên phiên bản: 1h x 3 nhánh x 4 phiên bản x N=3 (36 lần chạy). Xác nhận khả năng tổng quát hóa. | Kết quả xuyên phiên bản |
| **Ngày 9** | Tạo khung LaTeX: tiêu đề, abstract (với số placeholder), giới thiệu (vấn đề + giả thuyết), tài liệu liên quan (liệt kê 10 bài báo cần trích dẫn), phương pháp (3 phần: Nautilus gốc, thiết kế ngữ pháp, tích hợp RL), thí nghiệm, kết quả, kết luận. | `paper/main.tex` biên dịch được với các phần stub |
| **Ngày 10** | Viết phần Phương pháp từ code/docs hiện có. Tạo đường cong tăng trưởng coverage (matplotlib) và biểu đồ cột RC-count. Điền bảng kết quả với số liệu thực. | Phần phương pháp bài báo + 3-4 hình |

### Điểm quyết định quan trọng (cuối Tuần 1):

Nếu agent DQN **không có tín hiệu học** (Q-value không phân biệt, phân bố hành động giữ nguyên đồng đều, không cải thiện so với ngẫu nhiên), bạn cần quyết định:

- **(a)** Tái định khung thành bài báo kết quả tiêu cực ("RL không giúp ích cho fuzzing dựa trên ngữ pháp vì...") — vẫn có thể xuất bản
- **(b)** Thiết kế lại không gian state/reward/action trước khi mở rộng thí nghiệm
- **(c)** Thử phương pháp RL đơn giản hơn (multi-armed bandit, UCB) thay vì DQN

**Không** dành 2 tuần mở rộng thí nghiệm trên một kiến trúc không cho thấy tín hiệu học trong pilot.

---

## 6. Đánh Giá Trung Thực

### Những điểm vững chắc

- **Chất lượng kỹ thuật cao.** Codebase Rust được cấu trúc tốt (5.5k LOC qua 3 crate), tích hợp RL được thiết kế sạch sẽ (trait MutationPolicy, phân tách DqnPolicy/DefaultPolicy), harness/fork-server hoạt động chính xác, và pipeline triage (dedup, chấm điểm fidelity, chữ ký CVE) được suy nghĩ kỹ lưỡng.
- **Ablation E2 trung thực về mặt trí tuệ.** Báo cáo công khai nêu rằng giả thuyết ngữ pháp chắt lọc đã thất bại và trọng số không quan trọng ở khung thời gian 15 phút. Loại trung thực này hiếm và có giá trị — hãy sử dụng nó trong bài báo.
- **Hệ thống chấm điểm fidelity là mới mẻ.** Khớp chữ ký CVE dựa trên regex trên các mẫu được tạo, với chấm điểm theo từng pattern, là đóng góp có ý nghĩa cho phương pháp đánh giá grammar-fuzzing.

### Những điểm mơ hồ hoặc rủi ro

- **Đóng góp RL chỉ là vaporware.** Code tồn tại nhưng chưa bao giờ được đánh giá. Bạn không thể nộp bài báo với "Phase 3: Chưa bắt đầu" làm trạng thái của đóng góp cốt lõi.
- **Các khẳng định thống kê không được hỗ trợ.** N=2 không có kiểm định ý nghĩa. Báo cáo ablation hedge đúng cách nhưng bài báo đòi hỏi sự chặt chẽ.
- **Câu hỏi nghiên cứu không rõ ràng.** Đó là "RL cải thiện fuzzing"? "Thiết kế ngữ pháp quan trọng"? "Ngữ pháp nhận biết CVE thắng ngữ pháp generic"? Kết quả Phase 2 gợi ý câu trả lời cho hai câu sau là "không" ở khung thời gian ngắn. Bạn cần quyết định bài báo *nói về cái gì*.
- **cve2grammar mới tích hợp một nửa.** Ngữ pháp generated không thể chạy standalone, bước composition là một TODO, và 42 quy tắc tổng quát hóa bởi LLM chưa bao giờ được đánh giá như một ngữ pháp fuzzing.
- **Không có so sánh với công cụ bên ngoài.** Nếu không chạy Squirrel, AFL++, hoặc ít nhất Nautilus vanilla với ngữ pháp SQL generic làm baseline, reviewer sẽ hỏi "sao không dùng X?"

---

## 7. Kiểm Kê Codebase

### Các thành phần cốt lõi (Rust, tổng 5,577 LOC)

| Thành phần | File | LOC | Trạng thái |
|------------|------|-----|-----------|
| `fuzzer/src/main.rs` | 1 | 309 | Production — tích hợp RL đã nối dây nhưng chưa test với `rl_enabled: true` |
| `fuzzer/src/dqn.rs` | 1 | 422 | Hoàn chỉnh — DQN với replay buffer, target network, AdamW optimizer qua candle |
| `fuzzer/src/rl_hook.rs` | 1 | 122 | Hoàn chỉnh — trait MutationPolicy, DqnPolicy, DefaultPolicy |
| `fuzzer/src/rl_logger.rs` | 1 | 141 | Hoàn chỉnh — CSV logger cho RL metrics (tần suất action, Q-values, reward, loss) |
| `fuzzer/src/config.rs` | 1 | 88 | Hoàn chỉnh — Tất cả siêu tham số RL được expose qua config.ron |
| `fuzzer/src/dqn_test.rs` | 1 | 82 | Hoàn chỉnh — Forward pass đơn lẻ + test hội tụ |
| `grammartec/` | 10 | 2,441 | Production — Engine ngữ pháp với lấy mẫu có trọng số |
| `forksrv/` | 4 | 426 | Production — AFL fork server |

### Ngữ pháp (Python)

| Ngữ pháp | Quy tắc | Trạng thái |
|----------|---------|-----------|
| `sqlite_patterns.py` | ~99 NT | Baseline production |
| `sqlite_patterns_uniform.py` | ~99 NT | Biến thể bỏ trọng số |
| `sqlite_attack.py` | ~30 NT | Ngữ pháp tấn công chắt lọc (v2) |
| `sqlite_generated.py` | 42 quy tắc | KHÔNG tự chứa — tham chiếu 24 NT chưa định nghĩa |

### Pipeline Triage (Python)

| Module | LOC | Mục đích |
|--------|-----|---------|
| `triage/stack_dedup.py` | — | Dedup dựa trên stack-frame GDB |
| `triage/dedup.py` | 147 | Dedup bằng hash frame ASan |
| `triage/fidelity_score.py` | 119 | Chấm điểm fidelity cấu trúc theo pattern |
| `triage/cve_signatures.py` | 92 | Định nghĩa chữ ký CVE dựa trên regex (6 CVE) |
| `triage/report.py` | 192 | Trình tạo báo cáo crash Markdown |
| `triage/minimize.py` | — | Thu nhỏ crash SQL |

### Scripts

| Script | Mục đích |
|--------|---------|
| `scripts/run_eval.sh` | Launcher chiến dịch đơn |
| `scripts/run_ablation.sh` | Điều phối ablation 4 biến thể |
| `scripts/analyze.py` | Phân tích TTFC + coverage |
| `scripts/capture_coverage.py` | Trích xuất coverage từ exec.log |

### Kết quả Thí nghiệm (trên đĩa)

| Artifact | Vị trí | Nội dung |
|----------|--------|---------|
| Báo cáo ablation E2 | `docs/attack-grammar-ablation-sqlite-3.31.1.md` | 4 biến thể x 2 lần chạy, phân tích root-cause đầy đủ |
| Fidelity v1 baseline | `docs/fidelity-baseline-attack-v1.json` | Điểm fidelity trước B2 |
| Fidelity v2 sau B2 | `docs/fidelity-postB2-attack-v2.json` | Điểm fidelity sau B2 (P13435: 18.6%, P19646: 19.1%) |
| Dữ liệu chạy thô | `/tmp/nautilus_eval/` (tạm thời) | Không lưu vào git |

---

## 8. Các Phát Hiện Chính từ Thí Nghiệm Hiện Có

### Kết quả Ablation E2 (sqlite-3.31.1, 15 phút, N=2)

| Biến thể | Tổng Crash | Root Cause Duy nhất | Exec/giây |
|----------|-----------|-------------------|----------|
| attack_v1 (chắt lọc, trước B2) | 185 | 4 | ~230 |
| attack_v2 (chắt lọc, sau B2) | 53 | 2 | ~224 |
| patterns (thư viện đầy đủ, có trọng số) | 590 | 6 | ~99 |
| uniform (thư viện đầy đủ, không trọng số) | 592 | 6 | ~112 |

### Các kết luận chính

1. **Độ rộng từ vựng > chất lượng chắt lọc** ở khung thời gian 15 phút (patterns/uniform: 6 RC vs attack: 2-4 RC)
2. **Trọng số không quan trọng** ở khung thời gian này (patterns và uniform tìm cùng tập RC)
3. **Cải thiện fidelity không chuyển đổi thành crash** (attack_v2 có fidelity tốt hơn 10x trên P13435 nhưng tìm ít RC hơn)
4. **Ngữ pháp tấn công nhanh hơn 2x** về exec/giây nhưng vẫn tìm ít bug duy nhất hơn
