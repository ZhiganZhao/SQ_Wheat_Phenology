public class IsMomentRegistredZC_39
{
    public int isMomentRegistredZC_39;
    public IsMomentRegistredZC_39(int _isMomentRegistredZC_39)
    {
        isMomentRegistredZC_39=_isMomentRegistredZC_39;
    }
}

public static class Estimation_IsMomentRegistredZC_39
{
    public static IsMomentRegistredZC_39 CalculateIsMomentRegistredZC_39(List<string> calendarMoments)
    {


/*
     IsMomentRegistredZC39 Model

    Author: 
    Reference: Modeling development phase in the 
                Wheat Simulation Model SiriusQuality.
                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    Instituton: INRA Montpellier
    Abstract: if FlagLeafLiguleJustVisible is already Registred 
    
*/
        int isMomentRegistredZC_39;

        if (calendarMoments.Contains("FlagLeafLiguleJustVisible"))
        {
           isMomentRegistredZC_39 = 1 ;
        }
        else
            isMomentRegistredZC_39 = 0;
        return new IsMomentRegistredZC_39(isMomentRegistredZC_39);
    }
}

