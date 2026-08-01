import svgwrite
import random
import math
import os
from datetime import datetime

class VectorFlyerGenerator:
    def __init__(self):
        self.output_folder = "vector_flyers"
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
    
    def create_vector_flyer(self, title, description, details):
        # SVG dimensions (vector - can scale infinitely)
        width, height = 800, 1200
        
        # Create SVG drawing
        dwg = svgwrite.Drawing(size=(f"{width}px", f"{height}px"))
        
        # Add solid background (simpler than gradient)
        background_color = random.choice(['#2C3E50', '#34495E', '#1A5276', '#154360'])
        dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill=background_color))
        
        # Add mathematical background patterns (vector shapes)
        self.add_vector_patterns(dwg, width, height)
        
        # Add title
        dwg.add(dwg.text(
            title,
            insert=(width//2, 150),
            font_family="Arial",
            font_size=48,
            fill='white',
            text_anchor="middle",
            font_weight="bold"
        ))
        
        # Add description
        dwg.add(dwg.text(
            description,
            insert=(width//2, 250),
            font_family="Arial",
            font_size=24,
            fill='#E8F6F3',
            text_anchor="middle"
        ))
        
        # Add details
        y_position = 350
        for detail in details:
            dwg.add(dwg.text(
                f"• {detail}",
                insert=(100, y_position),
                font_family="Arial",
                font_size=20,
                fill='#D6EAF8'
            ))
            y_position += 40
        
        # Add vector mathematical elements
        self.add_mathematical_elements(dwg, width, height)
        
        return dwg
    
    def add_vector_patterns(self, dwg, width, height):
        """Add scalable vector patterns with proper SVG colors"""
        # Add grid pattern with proper color format
        grid_color = "#FFFFFF"
        for x in range(0, width, 50):
            dwg.add(dwg.line(
                start=(x, 0),
                end=(x, height),
                stroke=grid_color,
                stroke_width=0.5,
                stroke_opacity=0.1
            ))
        for y in range(0, height, 50):
            dwg.add(dwg.line(
                start=(0, y),
                end=(width, y),
                stroke=grid_color,
                stroke_width=0.5,
                stroke_opacity=0.1
            ))
        
        # Add vector circles with mathematical patterns
        colors = ['#E74C3C', '#3498DB', '#2ECC71', '#F39C12', '#9B59B6']
        for i in range(12):
            cx = random.randint(100, width - 100)
            cy = random.randint(100, height - 100)
            r = random.randint(15, 40)
            
            dwg.add(dwg.circle(
                center=(cx, cy),
                r=r,
                fill='none',
                stroke=random.choice(colors),
                stroke_width=1.5,
                stroke_opacity=0.3
            ))
    
    def add_mathematical_elements(self, dwg, width, height):
        """Add mathematical vector elements"""
        # Draw coordinate system
        center_x, center_y = width // 2, height // 2
        
        # Axes with proper colors
        dwg.add(dwg.line(
            start=(50, center_y),
            end=(width-50, center_y),
            stroke='white',
            stroke_width=2
        ))
        dwg.add(dwg.line(
            start=(center_x, 50),
            end=(center_x, height-50),
            stroke='white',
            stroke_width=2
        ))
        
        # Draw sine wave as vector path
        path_data = f"M 50 {center_y}"
        for x in range(50, width-50, 5):
            y = center_y + math.sin((x-50)/30) * 80
            path_data += f" L {x} {y}"
        
        dwg.add(dwg.path(
            d=path_data,
            fill='none',
            stroke='#E74C3C',
            stroke_width=2
        ))
        
        # Add mathematical symbols
        symbols = ["f(x)", "∫", "∑", "π", "∞", "∂"]
        for i, symbol in enumerate(symbols):
            x = 100 + i * 100
            y = height - 80
            dwg.add(dwg.text(
                symbol,
                insert=(x, y),
                font_family="Arial",
                font_size=24,
                fill='#85C1E9',
                font_style="italic"
            ))
    
    def save_as_svg(self, dwg, filename):
        """Save as vector SVG file"""
        dwg.saveas(filename)
        print(f"✓ Vector file saved: {filename}")
        return filename
    
    def generate_flyer(self, title, description, details):
        """Generate vector flyer"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Create vector flyer
        vector_dwg = self.create_vector_flyer(title, description, details)
        
        # Save SVG
        svg_filename = f"{self.output_folder}/vector_flyer_{timestamp}.svg"
        self.save_as_svg(vector_dwg, svg_filename)
        
        return {'svg': svg_filename}

def main():
    generator = VectorFlyerGenerator()
    
    # AI and Math themed content
    flyers = [
        {
            "title": "Vector AI Summit",
            "description": "Scalable AI solutions with mathematical foundations",
            "details": [
                "Neural Network Architectures",
                "Vector Mathematics Workshop", 
                "GPU Acceleration Techniques",
                "Real-time AI Applications"
            ]
        },
        {
            "title": "Mathematical Art Expo",
            "description": "Vector graphics meet algorithmic art generation",
            "details": [
                "Fractal Vector Art",
                "Algorithmic Design Patterns",
                "Interactive Math Visualizations",
                "Generative Art Workshops"
            ]
        },
        {
            "title": "Data Visualization Conference", 
            "description": "Transforming data into beautiful vector visualizations",
            "details": [
                "SVG Data Graphics",
                "Interactive Dashboards", 
                "Mathematical Plotting",
                "Real-time Data Streams"
            ]
        }
    ]
    
    print("🎨 Generating Vector-Based Flyers...")
    print("📐 Creating scalable SVG files...")
    
    for i, flyer in enumerate(flyers, 1):
        print(f"\nCreating flyer {i} of {len(flyers)}...")
        
        results = generator.generate_flyer(
            flyer["title"],
            flyer["description"], 
            flyer["details"]
        )
        
        for format_type, filename in results.items():
            print(f"  ✓ {format_type.upper()}: {filename}")
    
    print(f"\n✨ Vector flyer generation complete!")
    print(f"📁 Location: {os.path.abspath(generator.output_folder)}")
    print(f"\n💡 You can open SVG files in:")
    print(f"   - Web browsers (Chrome, Firefox, etc.)")
    print(f"   - Vector editors (Inkscape, Adobe Illustrator)")
    print(f"   - Office applications (Word, PowerPoint)")

if __name__ == "__main__":
    main()