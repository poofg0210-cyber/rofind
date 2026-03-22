import discord
from discord.ext import commands

import os
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

SERVERS = [
    {"name": "Blox Fruits", "size": "small", "members": 312, "desc": "Chill grinding server for Blox Fruits players.", "invite": "https://discord.gg/BrcQP8Nf"},
    {"name": "Ro-Trade", "size": "small", "members": 527, "desc": "Trusted small trading server with MM service.", "invite": "https://discord.gg/fantasyplays"},
    {"name": "BedWars", "size": "small", "members": 671, "desc": "Scrims, guides and tournaments for BedWars.", "invite": "https://discord.gg/het33KN7"},
    {"name": "infinidev", "size": "small", "members": 204, "desc": "Indie Roblox devs. Portfolio sharing and collab requests.", "invite": "https://discord.gg/infinidev"},
    {"name": "Piggy Towers", "size": "small", "members": 448, "desc": "Dedicated Piggy fan server. Strategy and lore theories.", "invite": "https://discord.gg/piggy-towers-community-server-1110668723615961159"},
    {"name": "Teutonnia Military RP", "size": "small", "members": 293, "desc": "Serious military roleplay. Events every weekend.", "invite": "https://discord.gg/teutonnia"},
    {"name": "Stylis (Phantom Forces)", "size": "small", "members": 822, "desc": "Casual and competitive Phantom Forces community.", "invite": "https://discord.gg/stylis"},
    {"name": "Dandy's World Unofficial", "size": "small", "members": 7719, "desc": "Runs, roleplays, events and giveaways for Dandy's World.", "invite": "https://discord.gg/dandysworld"},
    {"name": "Lilly's Garden", "size": "small", "members": 6562, "desc": "Safe and active Dandy's World community. Find runs and friends.", "invite": "https://discord.gg/lillysgarden"},
    {"name": "Grow A Garden Trades", "size": "small", "members": 3340, "desc": "Trading, giveaways and stock notifications for Grow A Garden.", "invite": "https://discord.gg/growagardentrades"},
    {"name": "Adopt Me Central", "size": "medium", "members": 5200, "desc": "Pet trading, giveaways and game updates.", "invite": "https://discord.gg/FuDGDsZQ"},
    {"name": "Blox Fruits Academy", "size": "medium", "members": 8700, "desc": "Fruit tier lists, guides and crew recruitment.", "invite": "https://discord.gg/bloxfruits"},
    {"name": "Arsenal Arena", "size": "medium", "members": 6100, "desc": "Competitive Arsenal players, LFG and rank pushing.", "invite": "https://discord.gg/arsenal-high-levels-785607778084323369"},
    {"name": "RoGang Roleplay", "size": "medium", "members": 3100, "desc": "Urban gang roleplay with faction wars and weekly events.", "invite": "https://discord.gg/ePnBEMMw"},
    {"name": "Tower of Hell Climbers", "size": "medium", "members": 2980, "desc": "Speed-run leaderboards, challenge rooms and tips.", "invite": "https://discord.gg/GTExTErD"},
    {"name": "Roblox Scripters United", "size": "medium", "members": 4400, "desc": "Monthly game jams, Lua help and portfolio showcases.", "invite": "https://discord.gg/tkQXygrW"},
    {"name": "Dandy's World Pro Community", "size": "medium", "members": 34999, "desc": "Focused on long and pro runs. Level up your Dandy's World game.", "invite": "https://discord.gg/dwpro"},
    {"name": "Grow A Garden (Stock Notifier)", "size": "medium", "members": 57101, "desc": "Auto stock notifier, trading and giveaways for Grow A Garden.", "invite": "https://discord.gg/growabiggarden"},
    {"name": "Rolimons", "size": "large", "members": 260802, "desc": "Biggest Roblox trading server. Limiteds, giveaways and MM.", "invite": "https://discord.gg/rolimons"},
    {"name": "RoBlox Hangout HQ", "size": "large", "members": 78000, "desc": "Most active general Roblox social server. Events and memes.", "invite": "https://discord.gg/gCBTAQTr"},
    {"name": "Deepwoken", "size": "large", "members": 521806, "desc": "Builds, races, dungeons and wipe announcements.", "invite": "https://discord.gg/deepwoken"},
    {"name": "Blox Fruits Official", "size": "large", "members": 3112514, "desc": "The official Blox Fruits community server.", "invite": "https://discord.gg/bloxfruits"},
    {"name": "Grow A Garden Official", "size": "large", "members": 4897579, "desc": "The official Grow A Garden server. Announcements, trading and events.", "invite": "https://discord.gg/gwQvzBS3Ea"},
]

@bot.event
async def on_ready():
    print(f"✅ RoFind is online as {bot.user}")
    print("Commands: !find <keyword> | !small | !medium | !large | !help_find")

@bot.command()
async def find(ctx, *, keyword=""):
    if not keyword:
        await ctx.send("❌ Please provide a keyword! Example: `!find blox fruits`")
        return
    keyword = keyword.lower()
    results = [s for s in SERVERS if keyword in s["name"].lower() or keyword in s["desc"].lower()]
    if not results:
        await ctx.send(f"❌ No servers found for **{keyword}**.\nTry: `blox fruits`, `trading`, `bedwars`, `adopt me`, `arsenal`, `deepwoken`, `roleplay`")
        return
    response = f"🔍 **Results for '{keyword}':**\n\n"
    for s in results[:5]:
        response += f"**{s['name']}** `{s['size'].upper()}` — {s['members']:,} members\n"
        response += f"_{s['desc']}_\n"
        response += f"🔗 {s['invite']}\n\n"
    await ctx.send(response)

@bot.command()
async def small(ctx):
    results = [s for s in SERVERS if s["size"] == "small"]
    response = "🟢 **Small Roblox Servers:**\n\n"
    for s in results:
        response += f"**{s['name']}** — {s['members']:,} members\n_{s['desc']}_\n🔗 {s['invite']}\n\n"
    await ctx.send(response)

@bot.command()
async def medium(ctx):
    results = [s for s in SERVERS if s["size"] == "medium"]
    response = "🟡 **Medium Roblox Servers:**\n\n"
    for s in results:
        response += f"**{s['name']}** — {s['members']:,} members\n_{s['desc']}_\n🔗 {s['invite']}\n\n"
    await ctx.send(response)

@bot.command()
async def large(ctx):
    results = [s for s in SERVERS if s["size"] == "large"]
    response = "🔴 **Large Roblox Servers:**\n\n"
    for s in results:
        response += f"**{s['name']}** — {s['members']:,} members\n_{s['desc']}_\n🔗 {s['invite']}\n\n"
    await ctx.send(response)

@bot.command()
async def help_find(ctx):
    await ctx.send(
        "**🤖 RoFind Bot Commands:**\n\n"
        "`!find <keyword>` — search by keyword (e.g. `!find blox fruits`)\n"
        "`!small` — list all small servers\n"
        "`!medium` — list all medium servers\n"
        "`!large` — list all large servers\n"
        "`!help_find` — show this help message"
    )

bot.run(TOKEN)
