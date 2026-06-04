# Team C6
2A202600765 - Cao Thị Thu Hà
2A202600709 - Hà Trung Kiên
2A202600873 - Nguyễn Lâm Phương Thảo
2A202600689 - Nguyễn Bình Huy

# Product SPEC: Coffeeholic 

*Tài liệu Đặc tả Sản phẩm (Day 06) - Nhóm Coffeeholic*

## 1. Bằng chứng (Evidence)
Nhu cầu giải quyết vấn đề xuất phát từ các quan sát thực tế và phân tích hành vi của người dùng mục tiêu:
- **Trải nghiệm trực tiếp:** Khi tìm kiếm không gian cafe với từ khóa như "yên tĩnh, cổ điển" trên bản đồ số, kết quả trả về đa phần thiếu chính xác do hệ thống ưu tiên từ khóa (keyword) thay vì cảm nhận thẩm mỹ (vibe). Việc người dùng thu thập hình ảnh trên các nền tảng mạng xã hội, sau đó đối chiếu lại địa chỉ tốn nhiều thời gian và làm gián đoạn trải nghiệm.
- **Khảo sát mạng xã hội:** Các từ khóa như "Review quán cafe", "quán cf Hà Nội/Sài Gòn" liên tục lọt top xu hướng (trending) trên nền tảng TikTok. Sự phát triển mạnh mẽ của hàng loạt hội nhóm chuyên chủ đề này trên Facebook minh chứng cho mức độ quan tâm đặc biệt lớn của giới trẻ đối với việc tìm kiếm các địa điểm có phong cách thẩm mỹ riêng. Mặc dù nhu cầu rất cao, họ vẫn gặp khó khăn trong việc diễn đạt chính xác sở thích đó bằng từ khóa văn bản trên các công cụ tìm kiếm truyền thống.

## 2. Lát cắt để build (Build slice)
Định hướng giải pháp cho **người dùng có nhu cầu tìm kiếm không gian cafe**: Nguyên mẫu (prototype) sẽ sử dụng AI hiển thị 3 hình ảnh đại diện ban đầu (Cold Start). Sau khi **người dùng lựa chọn hình ảnh phù hợp**, hệ thống sử dụng thuật toán Cosine Similarity để tính trung bình cộng vector của các ảnh đã chọn, từ đó **đề xuất danh sách 3 quán có độ tương đồng cao nhất về không gian** (có tối ưu về mặt khoảng cách di chuyển).

## 3. AI Product Canvas
- **Value (Giá trị):** Sản phẩm dành cho tập khách hàng chú trọng không gian thẩm mỹ nhưng gặp trở ngại khi đọc các bài đánh giá dài hoặc khó diễn đạt sở thích bằng từ khóa. AI hỗ trợ thay thế luồng tìm kiếm truyền thống bằng tương tác thị giác toàn diện (ra quyết định trực tiếp qua hình ảnh).
- **Trust (Niềm tin):** Khi AI đưa ra kết quả không tương đồng với lựa chọn ban đầu, người dùng có thể nhận diện ngay lập tức qua hình ảnh và hoàn tác bằng tính năng "Kết quả không phù hợp" để thiết lập lại thao tác. Kết quả của AI được đảm bảo độ tin cậy thông qua việc sử dụng tập dữ liệu nguồn đã được đội ngũ kiểm duyệt khắt khe từ trước.
- **Feasibility (Tính khả thi):** Nguyên mẫu có tính khả thi cao trong thời gian ngắn. Chi phí tính toán Cosine Similarity ở mức tối thiểu do sử dụng cơ sở dữ liệu tĩnh gồm 20-40 quán đã được phân loại và trích xuất đặc trưng vector (embedding) sẵn.
- **Tín hiệu học (Learning Signal):** Phản hồi "Kết quả không phù hợp" hoặc hành vi xem chi tiết lộ trình của một quán sẽ được hệ thống lưu lại, tạo nguồn dữ liệu để tối ưu hóa trọng số thuật toán gom cụm vector cho các phiên bản sau.

## 4. Tăng năng lực hay tự động hóa (Augment or Automate)
Sản phẩm được thiết kế theo hướng **Tăng năng lực (Augmentation)**.
- AI đảm nhiệm việc phân tích sở thích thị giác, xử lý lượng dữ liệu lớn để chắt lọc thành 3 đề xuất tối ưu nhất, tạo tiền đề cho quyết định của người dùng.
- **Lý do:** Sở thích thẩm mỹ là yếu tố mang tính chủ quan cao. Việc tự động hóa hoàn toàn (Automate) quá trình lựa chọn có thể dẫn đến rủi ro trải nghiệm kém, gây lãng phí thời gian và chi phí di chuyển của người dùng. Phương pháp "Tăng năng lực" giúp duy trì sự chủ động và trải nghiệm khám phá của khách hàng.

## 5. Bốn đường đi của trải nghiệm
- **Đường thuận (Happy Path):** AI xử lý với độ tin cậy cao. Người dùng chọn 1-2 hình ảnh đại diện -> AI đề xuất 3 quán có không gian tương đồng với đánh giá thực tế tốt -> Người dùng xem lộ trình và đưa ra quyết định.
- **Khi AI không chắc (Low-confidence):** AI gặp khó khăn do người dùng lựa chọn các hình ảnh mang phong cách hoàn toàn đối lập. Hệ thống thông báo: *"Rất khó để gợi ý chính xác không gian theo lựa chọn này"* và yêu cầu người dùng chỉ định lại 1-2 phong cách ưu tiên.
- **Khi AI sai (Failure):** Kết quả đề xuất không khớp với phong cách mong muốn. Người dùng sử dụng nút `Kết quả không phù hợp` để loại bỏ đề xuất hiện tại.
- **Khi người dùng sửa (Correction):** Thao tác `Kết quả không phù hợp` sẽ thiết lập lại giao diện hình ảnh ban đầu, đồng thời hệ thống ghi nhận tệp log (lịch sử sự kiện) về độ sai lệch của nhóm vector, phục vụ công tác kiểm thử và cải tiến thuật toán nội bộ.

## 6. Những kiểu lỗi đáng lo nhất
**Kiểu lỗi 1: Giảm độ chính xác của Model (Vector Cancellation)**
- *Nguyên nhân:* Dữ liệu đầu vào thiếu nhất quán (người dùng lựa chọn các bức ảnh mang phong cách hoàn toàn trái ngược nhau).
- *Hậu quả:* Hệ thống đưa ra các gợi ý thiếu tính đồng nhất, làm giảm trải nghiệm và độ tin cậy của ứng dụng.
- *Cách xử lý:* Giới hạn số lượng hình ảnh tối đa được phép chọn. Nếu điểm tương đồng (Cosine Score) ở mức thấp, hệ thống từ chối truy xuất và yêu cầu người dùng xác định lại ưu tiên.

**Kiểu lỗi 2: Sai lệch giữa hình ảnh và thực tế (Expectation vs. Reality Mismatch)**
- *Nguyên nhân:* Hệ thống phân tích hình ảnh chính xác, nhưng hình ảnh đầu vào đã qua chỉnh sửa quá mức, không phản ánh đúng không gian thực tế hoặc chất lượng dịch vụ đã xuống cấp.
- *Hậu quả:* Người dùng tốn thời gian và chi phí di chuyển nhưng trải nghiệm không như kỳ vọng, dẫn đến việc từ bỏ sử dụng ứng dụng.
- **Cách xử lý:** Áp dụng phương pháp kiểm soát chất lượng dữ liệu từ nguồn. Khác với việc thu thập dữ liệu tự động ồ ạt, cơ sở dữ liệu tĩnh sử dụng trong nguyên mẫu (MVP) được đội ngũ trực tiếp thẩm định và kiểm duyệt thủ công nhằm đảm bảo không gian thực tế khớp chính xác với hình ảnh cung cấp.

## 7. Kế hoạch kiểm thử và bằng chứng demo
- **Kịch bản tiêu chuẩn (Happy Case):** Lựa chọn 1 hình ảnh quán mang phong cách cổ điển (vintage). *Kỳ vọng:* AI đề xuất 3 quán có thiết kế tương đồng.
- **Kịch bản phức tạp (Corner Case):** Lựa chọn kết hợp 1 hình ảnh phong cách tối (dark-academia) và 1 hình ảnh không gian mở nhiều ánh sáng. *Kỳ vọng:* Hệ thống phát hiện độ nhiễu, hiển thị thông báo yêu cầu người dùng chọn lại thay vì xuất ra kết quả sai lệch.
- **Bằng chứng lưu giữ:** Đội ngũ lưu trữ tệp dữ liệu tĩnh (CSV/JSON), mã nguồn (script) tính toán vector và chuẩn bị sẵn video chạy thử nghiệm hai kịch bản trên nhằm phòng ngừa rủi ro kỹ thuật khi trình bày (demo).

## 8. Phân công
- **Huy:** Quản lý tài liệu chuyên môn (Product Canvas, Sơ đồ UX Flow), xây dựng nội dung trình bày (Slide) và trực tiếp thuyết trình.
- **Hà:** Thiết kế Frontend, chịu trách nhiệm kiểm thử hệ thống.
- **Kiên:** Xử lý và chuẩn bị cơ sở dữ liệu (Dataset tĩnh 30 quán, gắn nhãn hình ảnh và xuất dữ liệu vector embeddings).
- **Thảo:** Phát triển Backend (xây dựng logic thuật toán trung bình cộng Vector và Cosine Similarity, cung cấp API xuất kết quả).
