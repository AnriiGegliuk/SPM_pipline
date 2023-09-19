%Make barain mask from segmentated c1, c2, c3 maps
%brain strapping of DTI data
%clear all

cd G:\MRI\UT_11T\Yagishita_model\20220712_H483\T2\2nd

% c1=load_untouch_nii('c1b0_separate.nii');
% c2=load_untouch_nii('c2b0_separate.nii');
% c3=load_untouch_nii('c3b0_separate.nii');

c1=load_untouch_nii('c1T2.nii');
c2=load_untouch_nii('c2T2.nii');
c3=load_untouch_nii('c3T2.nii');


[x,y,z]=size(c1.img);
mask=zeros(x,y,z);

for n=1:z
    for k=1:y
        for m=1:x
          
            if c1.img(m,k,n)>0
                mask(m,k,n)=1;
            end
            
              if c2.img(m,k,n)>0
                mask(m,k,n)=1;
              end
                
              if c3.img(m,k,n)>0
                mask(m,k,n)=1;
              end
            
        end
    end
end

c1.img=mask;

save_untouch_nii(c1,'brain_mask.nii');