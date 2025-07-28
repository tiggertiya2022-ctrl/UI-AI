from aift import setting
 
setting.set_api_key('DsJCaRoXhwaW4Lik4cgYXC6kzFpRKm')
from aift.multimodal import textqa
 
result = textqa.generate('')

print(result['content'])