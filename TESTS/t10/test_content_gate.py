import unittest
from content_gate import assess
WEAK="""Nâng mũi đẹp không chỉ là nâng cao sống mũi — mà là tìm dáng phù hợp với tổng thể gương mặt.
Một dáng mũi hài hòa cần được cân nhắc theo đường nét khuôn mặt, mong muốn cá nhân và tình trạng mũi hiện tại. Vì vậy, trước khi lựa chọn phương án nâng mũi, hãy dành thời gian trao đổi rõ về dáng mũi mong muốn, khả năng thực hiện và những điều cần lưu ý trong quá trình chăm sóc.
Tại Dr. Sơn Aesthetic Clinic, khách hàng có thể bắt đầu bằng buổi tư vấn để tìm hiểu các lựa chọn phù hợp và được giải đáp những băn khoăn trước khi quyết định.
Muốn tìm hiểu về dịch vụ nâng mũi? Nhắn tin cho Dr. Sơn Aesthetic Clinic để được hướng dẫn đặt lịch tư vấn."""
BETTER="""Một chiếc mũi nhìn nghiêng cân đối chưa chắc đã hợp khi nhìn thẳng. Vì sao? Đường nét mũi cần được xem trong tương quan với toàn bộ khuôn mặt, không chỉ chiều cao sống mũi.
Khi tìm hiểu nâng mũi, có ba câu hỏi thực tế đáng đặt ra. Một: đầu mũi và da mũi hiện tại có những giới hạn nào? Hai: phương án bán cấu trúc hay cấu trúc được cân nhắc dựa trên điều gì? Ba: quá trình hồi phục và tái khám sẽ cần được giải thích ra sao? Các câu hỏi này không thể trả lời chính xác chỉ bằng một tấm ảnh.
Tại Dr. Sơn Aesthetic Clinic, khách hàng có thể liên hệ để trao đổi về mong muốn và sắp xếp thăm khám trực tiếp. Bác sĩ cần đánh giá cấu trúc thực tế trước khi tư vấn lựa chọn; không có phương án nào phù hợp với tất cả mọi người.
Nếu đang cân nhắc thay đổi dáng mũi, hãy gửi câu hỏi về điều bạn quan tâm nhất để được hướng dẫn bước tư vấn tiếp theo."""
WEAK_SECOND = """Một dáng mũi đẹp trên ảnh chưa chắc là dáng phù hợp với gương mặt bạn.
Ảnh tham khảo có thể giúp bạn diễn tả điều mình thích, nhưng không nên xem đó là khuôn mẫu để áp dụng cho tất cả. Khi tìm hiểu về nâng mũi, hãy thử làm rõ ba điều:
Bạn thích nét tự nhiên hay rõ nét hơn?
Khi nhìn chính diện và góc nghiêng, bạn muốn tổng thể gương mặt thay đổi như thế nào?
Với tình trạng mũi hiện tại, những lựa chọn nào có thể cân nhắc và cần lưu ý gì trong quá trình chăm sóc?
Một buổi tư vấn hữu ích nên giúp bạn hiểu thêm về các lựa chọn, giới hạn và điều cần cân nhắc trước khi quyết định — để bạn có thể chọn lựa một cách chủ động, không cần vội vàng.
Nếu đang tìm hiểu dịch vụ nâng mũi tại Dr. Sơn Aesthetic Clinic, hãy nhắn tin để hỏi lịch tư vấn. Bạn có thể gửi kèm ảnh dáng mũi mình yêu thích để bắt đầu trao đổi.
Bạn thích dáng mũi tự nhiên hài hòa hay đường nét rõ hơn? Chia sẻ lựa chọn của bạn nhé."""
class TestGate(unittest.TestCase):
 def test_reject_t10(self):
  r=assess(WEAK);self.assertEqual(r['screen'],'BLOCK')
  self.assertIn('HOOK_TEMPLATE',[x['id'] for x in r['issues']])
  self.assertIn('LOW_SERVICE_DETAIL',[x['id'] for x in r['issues']])
 def test_reject_second_t10_fixture(self):
  r=assess(WEAK_SECOND);self.assertEqual(r['screen'],'BLOCK')
  self.assertIn('QUESTIONNAIRE_WITHOUT_PAYOFF',[x['id'] for x in r['issues']])
 def test_better_not_automatically_pass(self):
  self.assertEqual(assess(BETTER)['screen'],'REVIEW_REQUIRED')
 def test_unsafe_claim(self):
  self.assertIn('UNSUPPORTED_PROMISE',[x['id'] for x in assess('Chúng tôi cam kết an toàn 100% cho mọi khách hàng')['issues']])
 def test_empty(self):self.assertEqual(assess('')['screen'],'BLOCK')
if __name__=='__main__':unittest.main()
