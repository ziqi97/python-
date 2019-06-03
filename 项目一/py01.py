menu = {
    '汽车': {
        '轿车': {
            '宝马': {
                '宝马760': {},
                '宝马M5': {},
                '宝马M3': {}
            },
            '奔驰': {
                '奔驰C180': {},
                '奔驰E260': {},
                '奔驰S600': {},
            },
            '奥迪': {
                '奥迪A4L': {},
            },
        },
        '越野车': {
            '保时捷': {
                '保时捷Macan': {},
                '保时捷Cayenne': {},
            },
            '路虎': {},
            '英菲尼迪': {},
        },
        '卡车': {},
        '公交车': {},
    },
    '飞机': {
        '大飞机': {
            "大1": {
                'xxx': {}
            }
        },
        '小飞机': {
            '小1': {
                'xxx': {}
            }
        },
        '直升机': {},
    },
    '大炮': {}
}


 
current_layer=menu
layers=[] #这里就相当于记录许多个字典
 
while True:
    for k in current_layer:
        print(k)
    choice=input('>>: ').strip()
 
    if choice == 'quit':break
 
    if choice == 'b':
        if len(layers) == 0:break
        current_layer=layers.pop()
        continue
 
    if choice not in current_layer:continue
 
    layers.append(current_layer) #记录好当前层
    current_layer=current_layer[choice]

