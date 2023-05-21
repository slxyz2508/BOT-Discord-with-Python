import discord
from discord.ext import commands
from discord import app_commands

class Embed(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @app_commands.command(name="ที่มา", description="ที่มาของIS")
    async def ที่มา(self, interaction:discord.Interaction):
        Embed_IS= discord.Embed(title="IS", description="สรุป IS แบบย่อๆ")
        Embed_IS.set_author(name="สรุป IS")
        Embed_IS.add_field(name="วัตถุประสงค์", value="1. เพื่อศึกษาการเขียนโค้ดด้วยภาษาไพทอน 2. เพื่อศึกษาการตอบกลับข้อความ อัตโนมัติ 3. เพื่อศึกษา UI ของระบบเบื้องต้น" , inline= False)     
        Embed_IS.add_field(name="ระยะเวลาและสถานที่ดำเนินการ", value="ระยะเวลาในการศึกษาค้นคว้าตั้งแต่วันที่ 15 เดือน ธันวาคม พ.ศ. 2565 ถึงวันที่ 5 เดือน มีนาคม พ.ศ. 2566 สถานที่ดำเนินการ ได้แก่ โรงเรียนบางปะกอกวิทยาคมและ บ้านส่วนตัว", inline= False)
        Embed_IS.add_field(name="ผลที่คาดว่าจะได้รับ", value="1. สามารถเรียนรู้ การเขียนโค้ดในภาษาไพทอน 2. เข้าใจระบบ ของ UI ตอบกลับข้อความอัตโนมัติ3. ช่วยพัฒนาทักษะที่ช่วยให้สามารถคิดอย่างเป็นเหตุเป็นผล ซึ่งจะส่งผลให้เกิดทักษะการแก้ปัญหาด้วยแนวคิดเชิงคำนวณ (Computational Thinking) 4.ส่งเสริมและช่วยในการแสดงออกทางความคิดสร้างสรรค์ เนื่องจากการเขียนโค้ดไม่ได้มีวิธีเดียว ดังนั้น จึงต้องคิดหาวิธีแก้ปัญหาหลาย ๆ อย่าง และมีความยืดหยุ่นในการแก้ปัญหา", inline= False)
        Embed_IS.add_field(name="อภิปรายผล", value="การเขียนโค้ดด้วยภาษาไพทอนเป็นภาษาที่เหมาะกับการเริ่มต้นที่จะเขียนทำให้สามารถเข้าใจระบบการตอบกลับของบอทดิสคอร์ด ทำให้สามารถนำไปพัฒนาต่อไปด้วยใช้แหล่งที่มาจากที่ที่ต้องการ เช่นทำบอทบอกข้อมูลภายในบริษัทให้กับลูกค้า หรือบอทให้ข้อมูลคนมาสอบถามข้อมูลในเว็ปไซต์ของโรงเรียน", inline=False)
        await interaction.response.send_message(embed=Embed_IS)
    
    @app_commands.command(name="คำสั่ง", description="คำสั่งทั้งหมด")
    async def คำสั่ง(self, interaction: discord.Interaction):
        Embed_help = discord.Embed(title="ชุดคำสั่ง", description="คำสั่งทั้งหมด")
        Embed_help.set_author(name="Krxt")
        Embed_help.add_field(name="ที่มา", value="แสดงจุดประสงค์ของการสร้างบอทตัวนี้ขึ้นมา", inline=False)
        Embed_help.add_field(name="กิต", value="แสดงผลตอบกลับมาในช่องแชทว่า 'เรื้อน'", inline=False)
        Embed_help.add_field(name="สัญญาณ", value="แสดงผลตอบกลับมาเป็นค่าความคลาดเคลื่อนหรือดีเลย์", inline=False)
        Embed_help.add_field(name="ข้าว", value="สุ่มคำตอบว่าข้าวเที่ยงอยากกินอะไร", inline=False)
        Embed_help.add_field(name="ผู้ใช้", value="แสดงข้อมูลของโปร์ไฟล์ผู้ใช้", inline=False)
        Embed_help.add_field(name="หา", value="หาข้อมูลต่างๆจากวิกิพีเดียโดยใช้ keyword", inline=False)
        Embed_help.add_field(name="ลิงก์", value="แสดงลิงก์ของเวปไซต์ที่ต้องการหาแล้วลิสต์เรียงลงมา(demo)", inline=False)
        Embed_help.add_field(name="แบบประเมิน", value="ช่วยทำแบบประเมินด้วยนะครับ")
        Embed_help.set_footer(text="ig: bjjad_ :โสด เรื้อน มีแมวชื่อพิกุล")
        await interaction.response.send_message(embed=Embed_help)
        
    @app_commands.command(name="แบบประเมิน", description="ช่วยทำหน่อยนะครับ")
    async def แบบประเมิน(self, interaction: discord.Interaction):
        Embed_Form = discord.Embed(title="แบบประเมิน", description="ช่วยทำหน่อยนะครับเพื่อการพัฒนาในอนาคต", color=discord.Color.blue())
        Embed_Form1 = discord.Embed(title="สมาชิก", color=discord.Color.orange())
        Embed_Form2 = discord.Embed(title="สมาชิก", color=discord.Color.purple())
        Embed_Form3 = discord.Embed(title="สมาชิก", color=discord.Color.red())
        Embed_Form.add_field(name="แบบประเมิน",value="https://docs.google.com/forms/d/e/1FAIpQLSfJ37ek3ycnMRwJ0YPx_1eJ2M2BQvBtjMQAs_u0GLYNnZmpMA/viewform?fbclid=IwAR2bSgx0YeUXRZXW6LZn_FHS1J9_Ws-mtWmK_oZ7KGY_rqDOIrw_ied-iHI")
        Embed_Form1.set_image(url="https://scontent.xx.fbcdn.net/v/t1.15752-9/280776506_1416467608780406_183616510844936992_n.jpg?stp=dst-jpg_s403x403&_nc_cat=101&ccb=1-7&_nc_sid=aee45a&_nc_eui2=AeE3xfqis4VoH2YrFiuLCi_UawHq_Vj-AZVrAer9WP4BlUuOqggJzNQBAJGBq0oLj-dSQRNWzZEHTQgq-Bn3RdE7&_nc_ohc=MX1sOO0o-EIAX_7DtGJ&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdT9djw1UY7t9Xdh7JXnWZlYNiBEUjs2C1CDEaurkdZjdw&oe=6447AF92")
        Embed_Form1.add_field(name="นายธนวัฒน์ มีชำนาญ เลขที่ 14", value="ทำทุกอย่าง เดอะแบกของกลุ่ม",inline=False)
        Embed_Form2.set_image(url="https://scontent.fbkk28-1.fna.fbcdn.net/v/t1.15752-9/327882310_1130851767601371_5665513642377880742_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeHFy_HXz1MY6v3zrE-0QbWpbO3Efuqc-vxs7cR-6pz6_Dsy5D0d0U9JATiJZsT4rV47R6eyDqMpt8c5pCtAA4M9&_nc_ohc=dwvsgrIRPFMAX8lwlUq&_nc_ht=scontent.fbkk28-1.fna&oh=03_AdTEoFAvnAeNXLgokvKzBWv0ZuD_i79A5U480YUCt1q7TQ&oe=6447953E")
        Embed_Form2.add_field(name="นายชิษณุพงศ์ รุ่งเรือง เลขที่ 20", value="พี่ก้อง Y2K สไลด์ดีเหมือนหน้าตา",inline=False)
        Embed_Form3.set_image(url="https://scontent.xx.fbcdn.net/v/t1.15752-9/329431771_739980384332343_2503461388940000851_n.jpg?stp=dst-jpg_s206x206&_nc_cat=105&ccb=1-7&_nc_sid=aee45a&_nc_eui2=AeHhmQpINC13aXeVYCw7qyFHO72Y7mWqeYM7vZjuZap5g1vuuFl_fvjzddkazUKHtLjShzsXRGi3pFYiw5v8RvKu&_nc_ohc=orcSkA0z-NUAX91stfP&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdRvcZQA5D0F5_w1F_SajZlHMuCof4i0-X1TG5bPLc4jZA&oe=6447AAB6")
        Embed_Form3.add_field(name="นายณฐภัทร กิตติสุทธิ์ เลขที่ 12", value="ปลาดุก คลังความรู้เคลื่อนที่",inline=False)
        embeds = [Embed_Form,Embed_Form1,Embed_Form2,Embed_Form3]
        await interaction.response.send_message(embeds=embeds)
        
async def setup(client):
    await client.add_cog(Embed(client))
