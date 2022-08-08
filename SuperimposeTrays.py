try:
    from PIL import Image
except ImportError:
    import Image

overlayBase = Image.open('resources/base/dt_top.png')

prefixes = ['', 'advanced_', 'dense_']

backgrounds = {'.steel' : '', '.galvanized_steel' : '_#BDBDBD', '.stainless_steel' : '_#839BAB'}

for prefix in prefixes:
    
    for k, v in backgrounds.items():    
    
        tray = Image.open('resources/base/' + prefix + 'distillation_tray.png')
        background = Image.open('resources/base/pump_machine_full' + v + '.png')
        background.paste(overlayBase, (0,0), overlayBase)
        background.paste(tray, (0,0), tray)  
        background.save(prefix + 'distillation_tray' + k + '.png')        




