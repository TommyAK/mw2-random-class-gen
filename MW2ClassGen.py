import random

def Menu():
    print("MW2 Class Generator!")
    print("This program will generate a random class.")
    print('----------------------------------------')
    print("Type 'y' to generate a random class.")
    print("Type 'n' to exit the program.")
    print('----------------------------------------')
    Choice()

def Choice():
    while True:
        answer = input("Input: ")
        if answer in ('n', 'y'):
            break
        print('Invalid input, must be "y" or "n"')
    if answer == 'n':
        exit("Exiting...")
    elif answer == 'y':
        Main()

def Main():
    print("Your Random Class:")
    print("----------------------------------------")
    p1 = random.choice(perk_1)
    if p1 == 'Bling':
        PrimaryBling()
        SecondaryBling()
        print('Perk 1:', p1)
    elif p1 == 'One Man Army':
        PrimaryNoBling()
        print('Secondary: No Secondary (OMA)')
        print('Perk 1:', p1)
    elif p1 != 'One Man Army' or 'Bling':
        PrimaryNoBling()
        SecondaryNoBling()
        print('Perk 1:', p1)
    p2 = perk_2
    random.shuffle(p2)
    for prk2 in range(1):
        print('Perk 2:', p2[prk2])
    p3 = perk_3
    random.shuffle(p3)
    for prk3 in range(1):
        print('Perk 3:', p3[prk3])
    ds = death_streaks
    random.shuffle(ds)
    for dest in range(1):
        print('Death Streak:', ds[dest])
    equip = equipment
    random.shuffle(equip)
    for eq in range(1):
        print('Equipment:', equip[eq])
    specg = special_grenades
    random.shuffle(specg)
    for sg in range(1):
        print('Special Grenade:', specg[sg])
    print("----------------------------------------")
    print("Type 'y' to generate another random class.")
    print("Type 'n' to exit the program.")
    Choice()


def Primary():
    primary = random.choice(assault_rifles + submachine_guns + light_machine_guns + sniper_rifles + riot_shield)
    return primary


def SecondaryNoBling():
    secondary = random.choice(machine_pistols + shotguns + handguns + launchers)
    if secondary in machine_pistols:
        attach1 = random.choice(mp_sights + mp_dualwield + mp_misc)
        print('Secondary:', secondary, '[', attach1, ']')
    elif secondary in shotguns:
        attach1 = random.choice(sg_sights + sg_misc)
        print('Secondary:', secondary, '[', attach1, ']')
    elif secondary in og_shotguns:
        attach1 = random.choice(ogsg_misc + ogsg_dualwield)
        print('Secondary:', secondary, '[', attach1, ']')
    elif secondary in handguns:
        attach1 = random.choice(hg_misc + hg_dualwield)
        print('Secondary:', secondary, '[', attach1, ']')
    elif secondary in og_handguns:
        attach1 = random.choice(oghg_misc + ogsg_dualwield)
        print('Secondary:', secondary, '[', attach1, ']')
    elif secondary in launchers:
        print('Secondary:', secondary)


def SecondaryBling():
    secondary = random.choice(machine_pistols + shotguns + handguns + launchers)
    if secondary in machine_pistols:
        attach1 = random.choice(mp_sights + mp_dualwield + mp_misc)
        attach2 = random.choice(mp_misc)
        if attach1 != attach2:
            print('Secondary:', secondary, '[', attach1, ']', '[', attach2, ']')
        else:
            Main()
    elif secondary in shotguns:
        attach1 = random.choice(sg_sights + sg_misc)
        attach2 = random.choice(sg_misc)
        if attach1 != attach2:
            print('Secondary:', secondary, '[', attach1, ']', '[', attach2, ']')
        else:
            Main()
    elif secondary in og_shotguns:
        attach1 = random.choice(ogsg_misc + ogsg_dualwield)
        attach2 = random.choice(ogsg_misc)
        if attach1 != attach2:
            print('Secondary:', secondary, '[', attach1, ']', '[', attach2, ']')
        else:
            Main()
    elif secondary in handguns:
        attach1 = random.choice(hg_misc + hg_dualwield)
        attach2 = random.choice(hg_misc)
        if attach1 != attach2:
            print('Secondary:', secondary, '[', attach1, ']', '[', attach2, ']')
        else:
            Main()
    elif secondary in og_handguns:
        attach1 = random.choice(oghg_misc + ogsg_dualwield)
        attach2 = random.choice(oghg_misc)
        if attach1 != attach2:
            print('Secondary:', secondary, '[', attach1, ']', '[', attach2, ']')
        else:
            Main()
    elif secondary in launchers:
        print('Secondary:', secondary)


def PrimaryBling():
    result = random.choice(assault_rifles + submachine_guns + light_machine_guns + sniper_rifles + riot_shield)
    if result in assault_rifles:
        attach1 = random.choice(ar_sights + ar_underbarrel + ar_misc)
        attach2 = random.choice(ar_misc)
        if attach1 != attach2:
            print('Primary:', result, '[', attach1, ']', '[', attach2, ']')
        else:
            Main()
    elif result in submachine_guns:
        attach1 = random.choice(smg_sights + smg_dualwield + smg_misc)
        attach2 = random.choice(smg_misc)
        if attach1 != attach2:
            print('Primary:', result, '[', attach1, ']', '[', attach2, ']')
        else:
            Main()
    elif result in light_machine_guns:
        attach1 = random.choice(lmg_sights + lmg_misc)
        attach2 = random.choice(lmg_misc)
        if attach1 != attach2:
            print('Primary:', result, '[', attach1, ']', '[', attach2, ']')
        else:
            Main()
    elif result in sniper_rifles:
        attach1 = random.choice(sniper_scopes + sniper_misc)
        attach2 = random.choice(sniper_misc)
        if attach1 != attach2:
            print('Primary:', result, '[', attach1, ']', '[', attach2, ']')
        else:
            Main()
    elif result in riot_shield:
        print('Primary:', result)


def PrimaryNoBling():
    result = Primary()
    if result in assault_rifles:
        attach1 = random.choice(ar_sights + ar_underbarrel + ar_misc)
        print('Primary:', result, '[', attach1, ']')
    elif result in submachine_guns:
        attach1 = random.choice(smg_sights + smg_dualwield + smg_misc)
        print('Primary:', result, '[', attach1, ']')
    elif result in light_machine_guns:
        attach1 = random.choice(lmg_sights + lmg_misc)
        print('Primary:', result, '[', attach1, ']')
    elif result in sniper_rifles:
        attach1 = random.choice(sniper_scopes + sniper_misc)
        print('Primary:', result, '[', attach1, ']')
    elif result in riot_shield:
        print('Primary:', result)


def NoSecondary():
    print('No Secondary (OMA)')


# Primary Weapons
assault_rifles = ['M4A1', 'FAMAS', 'SCAR-H', 'TAR-21', 'FAL', 'M16A4', 'ACR', 'F2000', 'AK-47']
submachine_guns = ['MP5K', 'UMP45', 'Vector', 'P90', 'Mini-Uzi']
light_machine_guns = ['L86 LSW', 'RPD', 'MG4', 'AUG HBAR', 'M240']
sniper_rifles = ['Intervention', 'Barrett .50cal', 'WA2000', 'M21 EBR']
riot_shield = ['Riot Shield']

# Secondary Weapons
machine_pistols = ['PP2000', 'G18', 'M93 Raffica', 'TMP']
shotguns = ['SPAS-12', 'AA-12', 'Striker', 'M1014']
og_shotguns = ['Ranger', 'Model 1887']
handguns = ['USP .45', 'M9']
og_handguns = ['.44 Magnum', 'Desert Eagle']
launchers = ['AT4-HS', 'Thumper', 'Stinger', 'Javelin', 'RPG-7']

# Assault Rifle Attachments
ar_sights = ['Red Dot Sight', 'ACOG Scope', 'Holographic Sight', 'Thermal Scope']
ar_underbarrel = ['Grenade Launcher', 'Shotgun Attachment']
ar_misc = ['Silencer', 'FMJ', 'Heartbeat Sensor', 'Extended Mags']

# Submachine Gun Attachments
smg_sights = ['Red Dot Sight', 'ACOG Scope', 'Holographic Sight', 'Thermal Scope']
smg_dualwield = ['Akimbo']
smg_misc = ['Rapid Fire', 'Silencer', 'FMJ', 'Extended Mags']

# Light Machine Gun Attachments
lmg_sights = ['Red Dot Sight', 'ACOG Scope', 'Holographic Sight', 'Thermal Scope']
lmg_misc = ['Grip', 'Silencer', 'FMJ', 'Heartbeat Sensor', 'Extended Mags']

# Sniper Rifle Attachments
sniper_scopes = ['ACOG Scope', 'Thermal Scope']
sniper_misc = ['Silencer', 'FMJ', 'Heartbeat Sensor', 'Extended Mags']

# Machine Pistol Attachments
mp_sights = ['Red Dot Sight', 'Holographic Sight']
mp_dualwield = ['Akimbo']
mp_misc = ['Silencer', 'FMJ', 'Extended Mags']

# Shotgun Attachments
sg_sights = ['Red Dot Sight', 'Holographic Sight', ]
sg_misc = ['Silencer', 'Grip', 'FMJ', 'Extended Mags']

# 1887 & Ranger Attachments
ogsg_dualwield = ['Akimbo']
ogsg_misc = ['FMJ']

# Handgun Attachments
hg_misc = ['FMJ', 'Silencer', 'Extended Mags', 'Tactical Knife']
hg_dualwield = ['Akimbo']

# .44 Revolver and Desert Eagle
oghg_misc = ['FMJ', 'Knife']
oghg_dualwield = ['Akimbo']

# Misc
equipment = ['Frag', 'Semtex', 'Throwing Knife', 'Tactical Insertion', 'Blast Shield', 'Claymore', 'C4']
special_grenades = ['Flash Grenade', 'Stun Grenade', 'Smoke Grenade']
death_streaks = ['Copycat', 'Painkiller', 'Martyrdom', 'Final Stand']

# Perks
perk_1 = ['Marathon', 'Sleight of Hand', 'Scavenger', 'Bling', 'One Man Army']
perk_2 = ['Stopping Power', 'Lightweight', 'Hardline', 'Cold-Blooded', 'Danger Close']
perk_3 = ['Commando', 'Steady Aim', 'Scrambler', 'Ninja', 'SitRep', 'Last Stand']

Menu()
