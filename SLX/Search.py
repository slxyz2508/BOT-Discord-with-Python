import discord
import wikipedia
from discord.ext import commands 
from discord import app_commands
import requests
from bs4 import BeautifulSoup

class Search(commands.Cog):
    def __init__(self, client):
        self.client = client
        
            
    @commands.command()
    async def หา(self, ctx, *, query):
        try:
            wikipedia.set_lang('th')
            page = wikipedia.page(query)
            title = page.title
            summary = page.summary.split('\n')[0]

            embed = discord.Embed(title=title, description=summary, url=page.url,color=0x00ff00)
            await ctx.send(embed=embed)
            
        except wikipedia.exceptions.DisambiguationError as e:
            options = '\n'.join(e.options)
            await ctx.send(f"Multiple results found. Please be more specific. Options:\n{options}")
            
        except wikipedia.exceptions.PageError:
            await ctx.send("Sorry, no page was found.")
              
            
    @commands.command()
    async def ลิงก์(self,  ctx, *, query):
        url = 'https://www.google.com/search?q=' + query
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        results = soup.find_all('a')
        links = []
        for r in results:
            link = r.get('href')
            if link.startswith('/url?q='):
                link = link[7:]
                if '&' in link:
                    link = link[:link.index('&')]
                links.append(link)
                if len(links) == 5:
                    break
        
        embed = discord.Embed(title=f"Search Results for '{query}'", color=discord.Color.blurple())
        for i, link in enumerate(links):
            embed.add_field(name=f"Result {i+1}", value=f"[{link}]({link})", inline=False)
        
        if not links:
            embed.description = "No search results found."
        
        await ctx.send(embed=embed)
   
        
async def setup(client):
    await client.add_cog(Search(client))



