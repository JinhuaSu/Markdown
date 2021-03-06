# 基于隐私保护视角的空间大数据生成
## 研究背景
- 互联网行业促进了大数据分析技术的发展，但是对于地理研究领域的互联网大数据分析依然存在许多困难，特别是数据质量与数据隐私问题。
- 其中，数据质量是很大的问题，比如说数据可信度低、部分数据缺失、数据集类别不平衡等。其中，数据集类别不平衡是较为普遍的一类问题，在地理研究所使用的新型地理大数据中，因为数据采集、数据采集群体的限制，所以会出现在某些类的样本数实际上是远少于其它类别的样本数的。因为类别不平衡，因此会导致对研究方法造成一定的困难，使得研究的结论产生些许偏差。对此的解决方法有很多，但其中最简单直接的方法，就是对数据集中的少类数据进行扩充，增加少类数据的绝对数量。对少类数据进行扩充，这种方法在图像识别领域已经被证实可以大大提高模型的准确度，因此，在未能收集到足够的数据的情形下，如何科学的扩充少类数据，成了机器学习中一个研究方向。
- 其次，数据隐私问题是大数据时代下的重要社会问题，也是数据共享环节必须要考虑的前提，国外研究将该具体任务命名为隐私保护的数据生成（privacy-preserving data publishing，PPDP）。数据采集的精细化使得数据潜在价值大大提升，数据挖掘技术因此快速发展，互联网公司过度采集用户信息，买卖用户信息成为引起广泛讨论的社会现象。数据的价值与隐私性使得企业与科研机构的数据共享存在壁垒，对数据共享的监管尺度难以把控，数据利用不够与数据滥用并存。近五年来，大型互联网企业的研究所成为资源丰富的研究宝地，传统科研机构相对被边缘化，但企业的商业属性决定了其数据利用的片面性，数据生成技术或成为促进数据共享的新通道。企业对个人数据的利用关注于具体的用户画像，存在对隐私数据的采集偏好，而科研机构对个人数据的利用关注于总体信息，对隐私数据相对不敏感。数据生成技术可以利用原始数据生成统计分析结果与真实情况相似的虚假数据，满足科研机构研究需求，同时从源头上切断了数据共享后数据泄露所造成的数据滥用风险。
- 互联网新型地理大数据大部分蕴含用户的位置信息，直接暴露了用户的行为活动，被滥用造成的后果是巨大的，空间数据生成的研究为新型地理数据的隐私保护和数据共享的矛盾关系提供了一条豁然大道。如何生成统计属性不变的虚假数据正在成为人工智能与地理研究的交叉热点。
## 