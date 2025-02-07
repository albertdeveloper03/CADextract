import os
import sys
import logging
from typing import Tuple, Optional
import ezdxf
from ezdxf.addons.drawing import Frontend, RenderContext
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
from ezdxf.tools.standards import linetypes
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from pathlib import Path

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DXFtoPDFConverter:
    """A class to handle DXF to PDF conversion with comprehensive error handling."""
    
    def __init__(self, input_path: str, output_path: str):
        """
        Initialize the converter with input and output paths.
        
        Args:
            input_path (str): Path to input DXF file
            output_path (str): Path for output PDF file
        """
        self.input_path = Path(input_path)
        self.output_path = Path(output_path)
        self.doc = None
        self.msp = None
        
    def validate_input_file(self) -> bool:
        """
        Validate the input DXF file exists and is readable.
        
        Returns:
            bool: True if file is valid, False otherwise
        """
        try:
            if not self.input_path.exists():
                raise FileNotFoundError(f"Input file not found: {self.input_path}")
            
            if not self.input_path.suffix.lower() == '.dxf':
                raise ValueError("Input file must be a DXF file")
            
            return True
            
        except Exception as e:
            logger.error(f"Input validation failed: {str(e)}")
            raise
    
    def validate_output_path(self) -> bool:
        """
        Validate the output directory exists and is writable.
        
        Returns:
            bool: True if path is valid, False otherwise
        """
        try:
            output_dir = self.output_path.parent
            if not output_dir.exists():
                output_dir.mkdir(parents=True)
                
            # Test if directory is writable
            test_file = output_dir / '.test_write'
            try:
                test_file.touch()
                test_file.unlink()
            except Exception:
                raise PermissionError(f"Output directory is not writable: {output_dir}")
            
            return True
            
        except Exception as e:
            logger.error(f"Output validation failed: {str(e)}")
            raise
    
    def load_dxf(self) -> None:
        """Load the DXF file and prepare it for conversion."""
        try:
            self.doc = ezdxf.readfile(self.input_path)
            self.msp = self.doc.modelspace()
            
            # Validate DXF version
            if self.doc.dxfversion < "AC1015":  # R2000
                raise ValueError("DXF version too old, minimum required version is R2000")
                
        except ezdxf.DXFStructureError as e:
            logger.error(f"Invalid or corrupted DXF file: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Failed to load DXF file: {str(e)}")
            raise
    
    def get_drawing_bounds(self) -> Tuple[Tuple[float, float], Tuple[float, float]]:
        """
        Calculate the bounds of the drawing.
        
        Returns:
            Tuple containing min and max points ((min_x, min_y), (max_x, max_y))
        """
        try:
            if not self.msp:
                raise ValueError("No modelspace available")
                
            bounds = self.msp.bbox()
            if bounds is None:
                raise ValueError("Unable to determine drawing bounds")
                
            return bounds.extmin, bounds.extmax
            
        except Exception as e:
            logger.error(f"Failed to calculate drawing bounds: {str(e)}")
            raise
    
    def convert_to_pdf(self) -> None:
        """Convert the DXF file to PDF using matplotlib as an intermediate step."""
        try:
            # Create matplotlib figure
            fig = plt.figure()
            ax = fig.add_axes([0, 0, 1, 1])
            
            # Create rendering context
            ctx = RenderContext(self.doc)
            ctx.set_current_layout(self.msp)
            
            # Create frontend
            frontend = Frontend(ctx, MatplotlibBackend(ax))
            
            # Render the drawing
            frontend.draw_layout(self.msp, finalize=True)
            
            # Save as PDF
            plt.savefig(
                self.output_path,
                format='pdf',
                dpi=300,
                bbox_inches='tight',
                pad_inches=0
            )
            plt.close()
            
            logger.info(f"Successfully converted {self.input_path} to {self.output_path}")
            
        except Exception as e:
            logger.error(f"Conversion failed: {str(e)}")
            raise
    
    def convert(self) -> bool:
        """
        Execute the full conversion process with error handling.
        
        Returns:
            bool: True if conversion was successful, False otherwise
        """
        try:
            logger.info(f"Starting conversion of {self.input_path}")
            
            # Run validation checks
            self.validate_input_file()
            self.validate_output_path()
            
            # Load and convert
            self.load_dxf()
            self.convert_to_pdf()
            
            return True
            
        except Exception as e:
            logger.error(f"Conversion failed: {str(e)}")
            return False

def main():
    """Main function to handle command line usage."""
    if len(sys.argv) != 3:
        print("Usage: python dxf_to_pdf.py <input_dxf_path> <output_pdf_path>")
        sys.exit(1)
        
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    converter = DXFtoPDFConverter(input_path, output_path)
    success = converter.convert()
    
    if success:
        print(f"Successfully converted {input_path} to {output_path}")
        sys.exit(0)
    else:
        print("Conversion failed. Check the log file for details.")
        sys.exit(1)

if __name__ == "__main__":
    main()