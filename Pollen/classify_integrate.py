from keras.models import Model
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing import image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

model = load_model(r"/Volumes/NRJ'S EHD/Mac/BE Project/InceptionFinal.h5")

def clf(path):
	index1={0:'Echium',1:'FuscosporaFusca',2:'FuscosporaTruncata',3:'Geniostoma',
	            4:'Griselinia',5:'Gunnera',6:'Ixerba',7:'Knightia',
	            8:'Kunzea',9:'Laurelia',10:'Lepto',11:'Lotus',12:'Manoao',
	            13:'Metrosideros',14:'Passiflora',15:'Taraxacum',16:'Typha'}

	description={
		    0:"Echium is a genus of approximately 70 species and several subspecies of flowering plant in the family Boraginaceae. The type species is Echium vulgare.Species of Echium are native to North Africa, mainland Europe to Central Asia and the Macaronesian islands, where it reaches its maximum diversity."

		    ,1:"No info available as of now"

		    ,2:"Nothofagus truncata is a species of tree endemic to New Zealand.Its common name derives from the fact that the timber has a high silica content, making it tough and difficult to sawHard beech is a tree up to 30m tall occurring in lowland and lower montane forest from latitude 35°S to 42°30'S, that is, from the north of the North Island southwards to Marlborough and south Westland in the South Island."

		    ,3:"Geniostoma is a genus of around 25 species of flowering plants in the family Loganiaceae. They are shrubs or small trees, with inflorescences borne in the axils of the simple, petiolate, oppositely-arranged leavesThe flowers are arranged in cymes, and each is pentamerous."

		    ,4:"Griselinia commonly known as kapuka, New Zealand broadleaf or pāpāuma is a fast-growing small to medium-sized evergreen tree that is native to New Zealand.It is a hardy evergreen shrub that grows up to about 10 metres tall."

		    ,5:"Gunnera is the sole genus of herbaceous flowering plants in the family Gunneraceae, which contains 63 species. Some species have extremely large leaves. Species in the genus are variously native to Latin America, Australia, New Zealand, Papuasia, Hawaii, insular Southeast Asia, Africa, and MadagascarThe stalks of many species are edible."

		    ,6:"No info available as of now"

		    ,7:"No info available as of now"

		    ,8:"Kunzea is a genus of plants in the family Myrtaceae and is endemic to Australasia. They are shrubs, sometimes small trees and usually have small, crowded, rather aromatic leaves. The flowers are similar to those of plants in the genus Leptospermum but differ in having stamens that are longer than the petals. Most kunzeas are endemic to Western Australia but a few occur in eastern Australia and a few are found in New Zealand. The taxonomy of the genus is not settled and is complicated by the existence of a number of hybrids."

		    ,9:"Laurelia is a genus of plant in the major group Angiosperms (flowering plants) in the family Atherospermataceae or formerly Monimiaceae. It contains only two species, both endemic to the southern hemisphere, an example of Gondwanan distribution."

		    ,10:"No info available as of now"

		    ,11:"No info available as of now"

		    ,12:"Manoao is a monotypic genus in the family Podocarpaceae. It is endemic to New Zealand. Before 1996 it was classified in genus Dacrydium or Lagarostrobos, but has recently been recognised as a distinct genus; some botanists still treat it in Lagarostrobos on the basis that it is not phylogenetically distinct from that genus. In molecular phylogenetic analyses Manoao was found to be related to Parasitaxu but their exact relationships are unresolved.Allergic symptoms include itching,skin rashes."

		    ,13:"Metrosideros is a genus of approximately 60 trees, shrubs, and vines mostly found in the Pacific region in the family Myrtaceae. Most of the tree forms are small, but some are exceptionally large, the New Zealand species in particular. The name derives from the Ancient Greek metra or'heartwood' and sideron or 'iron'. Perhaps the best-known species are the pōhutukawa, northern rātā, and southern rāta of New Zealand, and ʻōhiʻa lehua, from the Hawaiian Islands.Allergic symptoms include hay fever,itching,sneezing."

		    ,14:"Passiflora, known also as the passion flowers is a genus of about 550 species of flowering plants, the type genus of the family Passifloraceae.They are mostly tendril-bearing vines, with some being shrubs or trees. They can be woody or herbaceous. Passion flowers produce regular and usually showy flowers with a distinctive corona. The flower is pentamerous and ripens into an indehiscent fruit with numerous seeds.The allergic reaction due to this is itching, swelling, difficulty breathing, increased heart rate."

		    ,15:"Taraxacum is a large genus of flowering plant in the family Asteraceae,which consists of species commonly known as dandelions.The genus is native to Eurasia and North America. Like other members of the family they have very small flowers collected together into a composite flower head.Each single flower in a head is called a floret.In part due to their abundance along with being a generalist species dandelions are one of the most vital early spring nectar sources for a wide host of pollinators.The allergic  reactions due to pollen is hay fever,rashes on skin."

		    ,16:"Typha is a genus of about 30 species of monocotyledonous flowering plants in the family Typhaceae. These plants have a variety of common names, in British English as bulrush or reedmace in American English as reed, cattail or punks, in Australia as cumbungi or bulrush, in Canada as cattail, and in New Zealand as raupo. Other taxa of plants may be known as bulrush, including some sedges in Scirpus and related genera.The allergic reaction due to this are sneezing,puffiness of eyes,etc."
		}

	img=image.load_img(path,target_size=(500,500))
	x=image.img_to_array(img)
	import numpy as np
	x=np.expand_dims(x,axis=0)
	img_data=preprocess_input(x)
	img_data=img_data/500
	prediction=model.predict(img_data)
	m=max(list(prediction[0]))
	ans=index1[list(prediction[0]).index(m)]
	des=description[list(prediction[0]).index(m)]
	return [ans, des]
