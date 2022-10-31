import numpy as np 

class MedicalImaging:

    def match_patterns(self, scan_result, pattern):

        # make arrays out of the inputs
        p_array = self.to_array(pattern) 
        p_rows, p_cols = p_array.shape

        p_rot = self.different_rotations(p_array)
        n_rot = len(p_rot)
      
        s_array = self.to_array(scan_result)
        
        square = p_rows == p_cols

        # CASES: 
    # - Square pattern: no matter how many rotations, at most one matches the region
    # - Non-square pattern: has at least 2 rotations:
    #        -- 2 rotations: check each one independently
    #        -- 4 rotations: check each pair (of the same shape) indepently

        if square:
            n_matches = self.find_any_match(s_array, p_rot, shape = (p_rows, p_cols))
            return n_matches
        else: 
            h_patterns, v_patterns = p_rot[0], p_rot[1] if n_rot == 2 else (p_rot[0], p_rot[2]), (p_rot[1], p_rot[3])
            n_hmatches = self.find_any_match(s_array, h_patterns, shape = (p_rows,p_cols))
            n_vmatches = self.find_any_match(s_array, v_patterns, shape = (p_cols,p_rows)) #in this case the pattern is transposed
            n_matches = n_hmatches + n_vmatches
            return n_matches
      

    @staticmethod
    def to_array(pattern):
        return  np.array(list(map(list, pattern)))

    @staticmethod
    def different_rotations(pattern):
        # there are 4 possible rotations. 
        # The pattern can be fully symmetric (invariant under rotations) or have two symmetries or none at all
        # This is because of the subgroup structure of the cyclic group C4 
        # Therefore it is enough to check whether the first rotatation equals the original position, and otherwise if the second rotation equals the original position
        rot1 = np.rot90(pattern)
        if np.array_equal(rot1, pattern):
            return pattern,
        elif np.array_equal(rot2:=np.rot90(rot1), pattern):
            return pattern, rot1
        else:
            return pattern, rot1, rot2, np.rot90(rot2)
 
    @staticmethod
    def find_any_match(scan_result, patterns, **shape):
        # patterns are rotations grouped by shape
        s_rows, s_cols = scan_result.shape  
        p_rows, p_cols = shape['shape']
        n_matches = 0
     
        for i in range(s_rows-p_rows+1):
            for j in range(s_cols-p_cols+1):
                region = scan_result[i:i+p_rows,j:j+p_cols]
                    # for rotations of same shape only one rotation can match the region
                n_matches += int(any(np.array_equal(pattern, region) for pattern in patterns))
        return n_matches 



if __name__ == '__main__':
    result = MedicalImaging()
    #result.match_patterns([ " xx    x ", "   xx    ", "    x x  ", "   x  xx ", " xxx     " ], [ "x ", "xx" ])
    result.match_patterns([ "         ", "    *  **", "  ****   ", "    *    ", "   ***   " ], [ " * ", "***", " * " ])



    