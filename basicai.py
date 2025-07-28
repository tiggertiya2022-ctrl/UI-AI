from aift import setting
from aift.multimodal import vqa
 
setting.set_api_key('D3DsJCaRoXhwaW4Lik4cgYXC6kzFpRKm_KEY')

result = vqa.generate('image.jpg', 'บรรยายรูปนี้')
