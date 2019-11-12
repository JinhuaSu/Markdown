# BERTSUM_modify

## Problems
- labeling
- predict_combination

## Conceptions for improvement
- set-level classifier
- continuous label or loss

## Experiments
- traversing all permutation sets
- 0-1 labeling
- 0-1 sequence labeling
- rouge-score sequence labeling
- shuffle data with above experiments

## Problems reiteration
- label imbalance
- nonsense position attention
- risks more than rewards in the optimization

## Sensable solutions(AutoRegressive)
- memory mechanism in prediction
- tree-shape data set

## Schedule
- 2019-10-20 tree-shape data set
- 2019-10-24 train and test
- memory mechanism

## New direction
- BiSET: soft-template
- Monte calo tree
- greedy-combination tree

## calculate loss using tree-struction label
Assume that the model predict the summary sentences one by one using Auto-Regressive method. Firstly, the model predict the most possible sentence and put it into candidate set, additionally searching for its label in the first floor of the tree to calculate loss-1. Secondly, let the model know about which sentence has been predicted and use the model to predict the most conditionally-possible sentence, accordingly searching down through the first-predicted node and calculating the loss-2 based on the certain subtree. With similiar procedures, you could get the third-predicted tree and loss-3, or you could get more if you like. Pseudocode is in the following.

```py
model = bert(pretrain_config)
x = text_tokens4bert(input_text)
num_sentences = num_f(input_text)
y = label_tree
tree_depth = 3
loss = 0
pred_content = ''
node = x.root
for i in range(tree_depth):
    pred_vec = model.predict(x+bert_tokenize('[PRED]')+pred_content)
    pred_index = argsort(pred_vec,0)[-1]
    pred_content = find_sentence_tokens(input_text,pred_index)
    label_sequence = [1 if i in node.childs() else 0 for i in range(num_sentences)]
    loss_tmp = seq_norm_xen(pred_vec,label_sequence)
    loss += loss_tmp
    if node.find_child(pred_index):
        node = node.child(pred_index)
    else:
        loss += (tree_depth-1-i)
        break
model.backpropagation(loss)
```

## task
- problem
    + how to calculate