from ..FeatureExtractor import ContextFeatureExtractor

class sdss_petro_radius_g_err(ContextFeatureExtractor): 
        """What is the Petrosian radius error in arcsec?"""
        active = True
        extname = 'sdss_petro_radius_g_err' #extractor's name
        light_cutoff = 0.2 ## dont report anything farther away than this in arcmin
        
        verbose = False
        def extract(self):
                n = self.fetch_extr('intersdss')
                
                if n is None:
                    if self.verbose:
                        print "Nothing in the sdss extractor"
                    return None
                    
                if not n.has_key("in_footprint"):
                    if self.verbose:
                        print "No footprint info in the sdss extractor. Should never happen."
                    return None
                
                if not n['in_footprint']:
                    if self.verbose:
                        print "Not in the footprint"
                    return None

                if not n.has_key("petroRad_g_err"):
                    if self.verbose:
                        print "Desired parameter was not determined"
                    return None

                if not n.has_key("dist_in_arcmin"):
                    if self.verbose:
                        print "Desired parameter was not determined"
                    return None
                    
                if n["dist_in_arcmin"] > self.light_cutoff:
                    return None
                else:
                    rez = n["petroRad_g_err"]
                if self.verbose:
                        print n
                return rez