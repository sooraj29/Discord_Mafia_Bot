# bot.py
import os
import random
import time
import discord
from discord import Member
from discord.client import Client
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord import Intents
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')

guild=None
guild_id=749279965325033553

#roles
Vill_id=750618635441274971
Org_id=750618717171482694
Ch_id=750729490186895492
killed_id=750729589877243905
_def_id=750618365856317490
Vill=None
Org=None
Ch=None
killed=None
_def=None
gamest=0
eventst=0
vig_kc=0
mf=0
my=0
nu=0
vi=0
emoji=['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟','🇦','🇧','🇨','🇩','🇪','🇫','🇬','🇭','🇮','🇯','🇰','🇱','🇲','🇳','🇴','🇵','🇶','🇷','🇸','🇹','🇺','🇻','🇼','🇽','🇾','🇿']

#channels
cvill_id=750669706641408090
cmaf_id=750669731823878265
corg_id=750669765030445127
clp_id=750730215369474144
cf_id=750730317559758998
cm_id=750730374916734977
cn_id=750730422966812672
cvig_id=750730471675002982
cgen_id=749279965325033558
vvill_id=750730616944853134
vnit_id=753163777201012746
vded_id=751004767332991006
vgen_id=751039911297155072
sgame_id=843139903461392394
cvill=None
cgen=None
cmaf=None
corg=None
clp=None
cf=None
cm=None
cn=None
cvig=None
vvill=None
vnit=None
vded=None
sgame=None
vgen=None

#members
maf=[]
mafgod=0
lpm=[]
mcheck=0
nheal=0
vkill=0
fol=None
nhel=None
kil=[]
test1_id=750598465632862269
test2_id=431429131431968768
test1=None
test2=None
test=[test1,test2]
may=None
nur=None
v=None
night_ct=0

#nit
nt=0

# prefix
client = commands.Bot(command_prefix='!',intents=Intents.all())



#purge
@client.command('purge')
async def _purge(ctx,amount=1):
    await ctx.channel.purge(limit=amount)

#terminal use 
@client.event
async def on_ready():
    global guild
    guild=client.get_guild(guild_id)
    global eventst,Vill,Org,Ch,killed,_def,cvill,vnit,cmaf,corg,vgen,vded,clp,cf,cm,cn,cvig,vvill
    Vill=discord.utils.get(guild.roles, id=Vill_id)
    Org=discord.utils.get(guild.roles, id=Org_id)
    Ch=discord.utils.get(guild.roles, id=Ch_id)
    killed=discord.utils.get(guild.roles, id=killed_id)
    _def=discord.utils.get(guild.roles, id=_def_id)
    sgame=discord.utils.get(guild.stage_channels, id=sgame_id)
    cvill=discord.utils.get(guild.text_channels, id=cvill_id)
    cmaf=discord.utils.get(guild.text_channels, id=cmaf_id)
    corg=discord.utils.get(guild.text_channels, id=corg_id)
    clp=discord.utils.get(guild.text_channels, id=clp_id)
    cf=discord.utils.get(guild.text_channels, id=cf_id)
    cm=discord.utils.get(guild.text_channels, id=cm_id)
    cn=discord.utils.get(guild.text_channels, id=cn_id)
    cvig=discord.utils.get(guild.text_channels, id=cvig_id)
    vvill=discord.utils.get(guild.voice_channels, id=vvill_id)
    vnit=discord.utils.get(guild.voice_channels, id=vnit_id)
    vded=discord.utils.get(guild.voice_channels, id=vded_id)
    vgen=discord.utils.get(guild.voice_channels, id=vgen_id)
    test1=discord.utils.get(guild.members, id=test1_id)
    test2=discord.utils.get(guild.members, id=test2_id)
    cgen=discord.utils.get(guild.text_channels, id=cgen_id)
    print("bot has connected to Discord!")
    print('ROles been added')

@client.event
async def on_member_join(member):
    print(f'{member} joined the server')
    await Member.add_roles(member,_def)

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')


#commands

#remove_default
@client.command()
async def debug_on(ctx):
    for x in _def.members:
        if x.id!=test1_id and x.id!=test2_id:
            await discord.Member.remove_roles(x,_def)

#add_default
@client.command()
async def debug_off(ctx):
    for x in guild.members:
        if x.bot==False:
            await discord.Member.add_roles(x,_def)

#ready
@client.command()
async def ready(ctx):
    global eventst,gamest
    member=ctx.author
    if eventst==1:
        if gamest!=1:
            role=discord.utils.get(member.guild.roles, id=Vill_id)
            flag=1
            for x in member.roles:
                if x.id==Vill_id:
                    await ctx.send(f'{member.mention} is already a Villager')
                    flag=0
            if flag==1:
                await discord.Member.add_roles(member,role)
                await ctx.send(f'{member.mention} has been added to Villager')
        else:
            await ctx.send(f'{member.mention}, game is already going on. Wait for it to end')
    else:
        await ctx.send(f'{member.mention}, let the organiser start a event of mafia!!')
    


#remove
@client.command()
async def remove(ctx):
    global gamest
    member=ctx.message.author
    if gamest==0:
        role=discord.utils.get(member.roles, id=Vill_id)
        flag = 1
        for x in member.roles:
            if x.id == Vill_id :
                await discord.Member.remove_roles(member,role)
                flag=0
                await ctx.send(f'{member.mention} has been succesfully removed from Villager')
        if flag==1:
            await ctx.send(f'{member.mention} is not a Villager')
    else:
        await ctx.send(f'{member.mention}, game is already going on. Wait for it to end')


#eventmafia
@client.command()
async def event(ctx):
    member=ctx.message.author
    global eventst,Vill,Org,Ch,killed,_def,cvill,vnit,cmaf,corg,vgen,vded,clp,cf,cm,cn,cvig,vvill
    f=0
    for x in member.roles:
        if x.id==Org_id:
            f=1
    if f==1:
        if eventst==0:
            await ctx.send(f'A game of Mafia is starting.\n {_def.mention}\nJoin using **!ready**')
            eventst=1
        else:
            await ctx.send("The event of mafia is running!!!")
    else:
        await ctx.send(f'{member.mention} , only organisers can start an event')



#startmafia
@client.command()
async def start(ctx):
    member=ctx.message.author
    f=0
    global eventst,Vill,Org,Ch,killed,_def,cvill,vnit,cmaf,corg,vgen,vded,clp,cf,cm,cn,cvig,vvill,cgen
    global eventst
    global gamest
    for x in member.roles:
        if x.id==Org_id:
            f=1
    if f==1:
        if eventst==1:
            if gamest==1:
                await ctx.send("The game of mafia is running.\n Wait for it to end!!")
            else:
                await ctx.send(f'Heads up {Vill.mention} , the game is starting!!!!\nJoin the **Village** Voice channel')
                gamest=1
                for x in Vill.members:
                    await vvill.set_permissions(x,speak=True,connect=True)
        else:
            await ctx.send(f'{member.mention} ,start an event first using !event ')
    else:
        await ctx.send(f'{member.mention} , only organisers can start an game')
    # for x in Vill.members:
    #     await cgen.set_permissions(x,send_messages=False)


#endmafia
@client.command()
async def end(ctx,a):
    member=ctx.message.author
    f=0
    global eventst
    global gamest,Vill,cmaf,clp,cf,cm,cn,cvig,cvill,vvill,vded,vgen
    for x in member.roles:
        if x.id==Org_id:
            f=1
    if f==1:
        gamest=0
        eventst=0
        if a=='m' or a=='M':
            await ctx.send('Mafia win the game!!!!!')
        elif a=='v' or a=='V':
            await ctx.send('Villagers win the game!!!!!!')
        elif a=='l' or a=='L':
            await ctx.send('Lover Pair win the game!!!!!!')
        for x in Vill.members:
            for y in [cmaf,clp,cf,cm,cn,cvig]:
                await y.set_permissions(x,read_messages=False,send_messages=False)
            await discord.Member.remove_roles(x,Vill)
        for x in killed.members:
            await discord.Member.remove_roles(x,killed)
        for x in vvill.members:
            await x.move_to(vgen)
        for y in vded.members:
            await y.move_to(vgen)                 
    else:
        await ctx.send(f'{member.mention} , only organisers can end a game')        

#night
@client.command()
async def nit(ctx):
    member=ctx.message.author
    f=0
    global Vill,Org,Ch,killed,_def,gamest,eventst,vig_kc,mf,my,nu,vi,cvill,cgen,cmaf,corg,clp,cf,cm,cn,cvig,vvill,vnit,vded,sgame,vgen,maf,lpm,fol,may,v,night_ct,nur
    for x in member.roles:
        if x.id==Org_id:
            f=1
    if f==1:
        nt=1
        mf=my=nu=vi=1
        await cvill.send(f'{Vill.mention} night time has fallen')
        await cmaf.send('Mafia, whom do u choose to kill?\n The people living are: \n')
        await cn.send('Nurse, whom do u wanna choose to save?')
        await cvig.send(f'Vigilante, whom do u wanna kill\nYou have {vig_kc} bullets left..')
        await cm.send('Mayor, whom do u wanna check?')
        for x in vvill.members:
            await x.move_to(vnit)
        for x in Vill.members:
            await cvill.set_permissions(x,send_messages=False)
            await cmaf.send(f'{x.mention}')
    else:
        await ctx.send(f'{member.mention} , only organisers can use the command')
    for x in maf:
        await cmaf.set_permissions(x,send_messages=True,read_messages=True)
    if may!=None:
        await cm.set_permissions(may,send_messages=True,read_messages=True)
    if nur!=None:
        await cn.set_permissions(nur,send_messages=True,read_messages=True)
    if v!=None:
        await cvig.set_permissions(v,send_messages=True,read_messages=True)
    for x in lpm:
        await clp.set_permissions(x,send_messages=True,read_messages=True)
    if fol!=None:
        await cf.set_permissions(fol,send_messages=True,read_messages=True)
    if(night_ct!=0):
        for x in lpm:
            await clp.set_permissions(x,send_messages=False,read_messages=True)
    night_ct+=1
    
#day
@client.command()
async def day(ctx):
    member=ctx.message.author
    f=0
    global Vill,Org,Ch,killed,kil,nheal,mcheck,nhel,vkill,_def,gamest,eventst,vig_kc,mf,my,nu,vi,cvill,cgen,cmaf,corg,clp,cf,cm,cn,cvig,vvill,vnit,vded,sgame,vgen,maf,lpm,fol,may,v,night_ct,nur
    for x in member.roles:
        if x.id==Org_id:
            f=1
    if f==1:
        nt=0
        mf=my=nu=vi=0
        await cvill.send(f'{Vill.mention} sunrise')
        for x in vnit.members:
            await x.move_to(vvill)
        #lpkill()
        for x in kil:
            if x.id==nheal:
                kil.remove(x)
                break
        k=0
        for x in lpm:
            for y in kil:
                if x==y:
                    k=1
        if k==1:
            for x in lpm:
                kil.append(x)
        kil = list(dict.fromkeys(kil))
        for x in kil:
            if x.id==nheal:
                kil.remove(x)
                break
        for x in kil:
            await cvill.send(f'{x.mention} has been killed!!!')
            await discord.Member.add_roles(x,killed)
            await discord.Member.remove_roles(x,Vill)
            await x.move_to(vded)
            for y in [cmaf,clp,cf,cm,cn,cvig]:
                await y.set_permissions(x,read_messages=False,send_messages=False)
            await vvill.set_permissions(x,speak=False)
            await cvill.set_permissions(x,read_messages=True,send_messages=False)
        for x in Vill.members:
            await cvill.set_permissions(x,send_messages=True)
        kil.clear()
        mcheck=0
        nheal=0
        nhel=None
        vkill=0   
        for x in maf:
            await cmaf.set_permissions(x,send_messages=False,read_messages=True)
        if may!=None:
            await cm.set_permissions(may,send_messages=False,read_messages=True)
        if nur!=None:
            await cn.set_permissions(nur,send_messages=False,read_messages=True)
        if v!=None:
            await cvig.set_permissions(v,send_messages=False,read_messages=True)
        for x in lpm:
            await clp.set_permissions(x,send_messages=False,read_messages=True)
        if fol!=None:
            await cf.set_permissions(fol,send_messages=False,read_messages=True)
    else:
        await ctx.send(f'{member.mention} , only organisers can use the command')


#kill
@client.command()
async def kill(ctx,mem:discord.ext.commands.MemberConverter):
    member=ctx.message.author
    f=0
    global Vill,cvill,cmaf,cn,cvig,cm,nt,mf,my,nu,vi,nt,gamest,eventst
    for x in member.roles:
        if x.id==Org_id:
            f=1
    #lpkill()
    if f==1:
        if mem!=fol:
            await cvill.send(f'{mem.mention} has been killed')
            await discord.Member.add_roles(mem,killed)
            await discord.Member.remove_roles(mem,Vill)
            await mem.move_to(vded)
            await vvill.set_permissions(mem,speak=False)
            await cvill.set_permissions(x,read_messages=True,send_messages=False)
            for y in [cmaf,clp,cf,cm,cn,cvig]:
                await y.set_permissions(mem,read_messages=False,send_messages=False)     
        else:
            gamest=0
            eventst=0
            await ctx.send('Fool win the game!!!!!!')
            for x in Vill.members:
                for y in [cmaf,clp,cf,cm,cn,cvig]:
                    await y.set_permissions(x,read_messages=False,send_messages=False)
                await discord.Member.remove_roles(x,Vill)
            for x in killed.members:
                await discord.Member.remove_roles(x,killed)
    else:
        await ctx.send(f'{member.mention}, only organisers can use the command')
















#mafia_god_selection
@client.command()
async def godfather(ctx,mem:discord.ext.commands.MemberConverter):
    f=0
    k=0
    global Vill,cmaf,cn,cvig,cm
    global mafgod
    member=ctx.message.author
    for x in member.roles:
        if x.id==Org_id:
            f=1
    if f==0:
        await ctx.send('Only usable by organiser!!')
    else:
        for x in cmaf.members:
            if x.id==mem.id:
                mafgod=mem.id
                k=1
                await ctx.send(f'{mem.mention} is the god father!')
        if k==0:
            await ctx.send(f'{mem.mention} is not a mafia')
        

#day_voting
@client.command()
async def dvot(ctx):
    f=0
    i=0
    mes=None
    member=ctx.message.author
    global emoji
    for x in member.roles:
        if x.id==Org_id:
            f=1
    if f==0:
        await ctx.send('Only usable by Organisers!!!')
    else:
        await ctx.send('Poll:')
        for x in Vill.members:
            await ctx.send(f'{emoji[i]}:{x.mention}')
            i+=1
        mes=cvill.last_message 
        for x in range(0,i):
            await mes.add_reaction(emoji[x])


#mafia_kill
@client.command()
async def mk(ctx,mem:discord.ext.commands.MemberConverter):
    f=k=0
    global Vill,cmaf,cn,cvig,cm,kil,mf
    member=ctx.message.author
    for x in cmaf.members:
        if x.id==member.id:
            f=1
    for x in Org.members:
        if x==mem:
            k=1
    if f==0:
        await ctx.send('Not usable by you!!')
    if k==1:
        await ctx.send('How :regional_indicator_d::regional_indicator_a::regional_indicator_r::regional_indicator_e: you kill the Organiser')
    elif mf==1:
        kil.append(mem)
        mf=0
        await cmaf.send(f'you have chosen to kill {mem.mention}')

    else:
        await cmaf.send('Not able to use command!!')

#mayor_check
@client.command()
async def check(ctx,mem:discord.ext.commands.MemberConverter):
    f=k=0
    global Vill,cmaf,cn,cvig,cm,mcheck,mafgod,my
    member=ctx.message.author
    for x in cm.members:
        if x.id==member.id:
            f=1
    for x in Org.members:
        if x==mem:
            k=1
    if f==0:
        await ctx.send('Not usable by you!!')
    if k==1:
        await ctx.send('How :regional_indicator_d::regional_indicator_a::regional_indicator_r::regional_indicator_e: you check the Organiser')
    elif my==1:
        mcheck=mem
        my=0
        p=0
        for x in maf:
            if x==mcheck:
                if mcheck.id!=mafgod:
                    await cm.send(f'{mem.mention} is a mafia!!!')
                    p=1
        if p==0:
            await cm.send(f'{mem.mention} is not a mafia!!')
    else:
        await cm.send('Not able to use command!!')



#nurse_heal
@client.command()
async def heal(ctx,mem:discord.ext.commands.MemberConverter):
    f=0
    global Vill,cmaf,cn,cvig,cm,nheal,nu,nhel
    member=ctx.message.author
    for x in cn.members:
        if x.id==member.id:
            f=1
    for x in Org.members:
        if x==mem:
            k=1
    if f==0:
        await ctx.send('Not usable by you!!')
    if k==1:
        await ctx.send('How :regional_indicator_n::regional_indicator_i::regional_indicator_c::regional_indicator_e: of you to heal the Organiser,\n But no thanks, choose a fellow Villager')
    elif nu==1:
        nheal=mem.id
        nhel=mem
        nu=0
        await cn.send(f'you have chosen to heal {mem.mention}')

    else:
        await cn.send('Not able to use command!!')


#vigilante_kill
@client.command()
async def vk(ctx,mem:discord.ext.commands.MemberConverter):
    f=0
    global Vill,cmaf,cn,cvig,cm,vig_kc,vkill,kil,vi
    member=ctx.message.author
    for x in cvig.members:
        if x.id==member.id:
            f=1
    for x in Org.members:
        if x==mem:
            k=1
    if f==0:
        await ctx.send('Not usable by you!!')
    if k==1:
        await ctx.send('How :regional_indicator_d::regional_indicator_a::regional_indicator_r::regional_indicator_e: you kill the Organiser')
    elif vi==1:
        if vig_kc>0:
            vkill=mem.id
            kil.append(mem)
            vi=0
            await cvig.send(f'you have chosen to kill {mem.mention}')
            vig_kc-=1
        else:
            await cvig.send('Out of bullets!!')
    else:
        await cvig.send('Not able to use command!!')

#godfather_voting
@client.command()
async def godvot(ctx):
    f=0
    i=0
    mes=None
    member=ctx.message.author
    global emoji
    for x in Org.members:
        if x==member:
            f=1
    if f==0:
        await ctx.send('Only usable by Organisers!!!')
    else:
        await ctx.send('Poll:')
        for x in maf:
            await ctx.send(f'{emoji[i]}:{x.mention}')
            i+=1
        mes=cmaf.last_message 
        for x in range(0,i):
            await mes.add_reaction(emoji[x])















































#mafia_channel
@client.command()
async def mafia(ctx,mem:discord.ext.commands.MemberConverter):
    global Vill,cmaf,cn,cvig,cm,maf
    if ctx.channel.id != corg_id:
        await ctx.send("Cannot use this command in this channel.\n Head to organisers channel")
    else:
        for x in mem.roles:
            if x==Vill:
                for y in ctx.guild.text_channels:
                    if y.id==cmaf_id:
                        await y.set_permissions(mem,read_messages=True,send_messages=True)
    maf.append(mem)
            # else:
            #     await ctx.send(f'{x.mention} is not a villager')


#mayor_channel
@client.command()
async def mayor(ctx,mem:discord.ext.commands.MemberConverter):
    global Vill,cmaf,cn,cvig,cm,may
    if ctx.channel.id != corg_id:
        await ctx.send("Cannot use this command in this channel.\n Head to organisers channel")
    else:
        for x in mem.roles:
            if x==Vill:
                for y in ctx.guild.text_channels:
                    if y.id==cm_id:
                        await y.set_permissions(mem,read_messages=True,send_messages=True)
            # else:
            #     await ctx.send(f'{x.mention} is not a villager')
    may=mem

#nurse_channel
@client.command()
async def nurse(ctx,mem:discord.ext.commands.MemberConverter):
    global Vill,cmaf,cn,cvig,cm,nur  
    if ctx.channel.id != corg_id:
        await ctx.send("Cannot use this command in this channel.\n Head to organisers channel")
    else:
        for x in mem.roles:
            if x==Vill:
                for y in ctx.guild.text_channels:
                    if y.id==cn_id:
                        await y.set_permissions(mem,read_messages=True,send_messages=True)
            # else:
            #     await ctx.send(f'{x.mention} is not a villager')
    nur=mem

#vigilante_channel
@client.command()
async def vigil(ctx,mem:discord.ext.commands.MemberConverter):
    global Vill,cmaf,cn,cvig,cm,v
    if ctx.channel.id != corg_id:
        await ctx.send("Cannot use this command in this channel.\n Head to organisers channel")
    else:
        for x in mem.roles:
            if x==Vill:
                for y in ctx.guild.text_channels:
                    if y.id==cvig_id:
                        await y.set_permissions(mem,read_messages=True,send_messages=True)
    v=mem


#vigilante_bullets
@client.command()
async def bullet(ctx,a):
    a=int(a)
    global vig_kc,cvig
    if ctx.channel.id != corg_id:
        await ctx.send("Cannot use this command in this channel.\n Head to organisers channel")
    else:
        vig_kc=a
        await ctx.send(f'You have given Vigilante, {vig_kc} bullets')
        await cvig.send(f'You are given {vig_kc} bullets!!!')

#lover_pair_channel
@client.command()
async def lp(ctx,mem1:discord.ext.commands.MemberConverter,mem2:discord.ext.commands.MemberConverter):
    global Vill,cmaf,cn,cvig,cm,lpm
    if ctx.channel.id != corg_id:
        await ctx.send("Cannot use this command in this channel.\n Head to organisers channel")
    else:
        for x in mem1.roles:
            if x==Vill:
                for y in ctx.guild.text_channels:
                    if y.id==clp_id:
                        await y.set_permissions(mem1,read_messages=True,send_messages=True)
            # else:
            #     await ctx.send(f'{mem1.mention} is not a villager')
        for x in mem2.roles:    
            if x==Vill:
                for y in ctx.guild.text_channels:
                    if y.id==clp_id:
                        await y.set_permissions(mem2,read_messages=True,send_messages=True)
    lpm=[mem1,mem2]
            # else:
            #     await ctx.send(f'{mem2.mention} is not a villager')


#fool_channel
@client.command()
async def fool(ctx,mem:discord.ext.commands.MemberConverter):
    global Vill,cmaf,cn,cvig,cm,fol
    if ctx.channel.id != corg_id:
        await ctx.send("Cannot use this command in this channel.\n Head to organisers channel")
    else:
        for x in mem.roles:
            if x==Vill:
                for y in ctx.guild.text_channels:
                    if y.id==cf_id:
                        await y.set_permissions(mem,read_messages=True,send_messages=True)
    fol=mem
            # else:
            #     await ctx.send(f'{x.mention} is not a villager')








client.run(TOKEN)
